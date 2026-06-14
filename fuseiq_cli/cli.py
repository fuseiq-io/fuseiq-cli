"""
fuseiq CLI — deploy, status, and logs for your FuseIQ agents.

Usage:
    fuseiq deploy <script>
    fuseiq status
    fuseiq logs <name>
"""

import argparse
import sys
import os
import json


def cmd_deploy(script_path):
    """Upload a Python script as a new agent and start its heartbeat."""
    if not os.path.isfile(script_path):
        print(f"Error: file not found — {script_path}", file=sys.stderr)
        sys.exit(1)

    agent_name = os.path.splitext(os.path.basename(script_path))[0]
    print(f"Deploying agent '{agent_name}' from {script_path}")

    # MVP: metadata-only deploy. Future: actually upload to FuseIQ API.
    metadata = {
        "agent": agent_name,
        "script": script_path,
        "status": "registered",
    }
    metadata_path = f".fuseiq_{agent_name}.json"
    with open(metadata_path, "w") as f:
        json.dump(metadata, f, indent=2)

    print(f"  Agent:      {agent_name}")
    print(f"  Script:     {script_path}")
    print(f"  Metadata:   saved to {metadata_path}")
    print(f"  Dashboard:  https://fuseiq.io/dashboard")
    print()
    print(f"To start the agent, run: python {script_path}")


def cmd_status():
    """List all registered agents (MVP: show link to dashboard)."""
    print("Registered agents:")
    print("  View your agents and their live status at:")
    print("  https://fuseiq.io/dashboard")
    print()
    print("(Local agent metadata files found:)")

    count = 0
    for f in os.listdir("."):
        if f.startswith(".fuseiq_") and f.endswith(".json"):
            with open(f) as fh:
                data = json.load(fh)
            print(f"  - {data.get('agent', f)} ({data.get('status', 'unknown')})")
            count += 1

    if count == 0:
        print("  (none — deploy an agent first with `fuseiq deploy <script>`)")


def cmd_logs(name):
    """Show logs for a specific agent (MVP: link to dashboard)."""
    print(f"Logs for agent '{name}':")
    print(f"  View live logs and metrics at:")
    print(f"  https://fuseiq.io/dashboard/{name}")
    print()
    print("(In a future version, tail logs will be available from the CLI.)")


def main():
    parser = argparse.ArgumentParser(description="FuseIQ CLI — agent deployment & management")
    sub = parser.add_subparsers(dest="command", required=True)

    deploy_parser = sub.add_parser("deploy", help="Register a Python script as an agent")
    deploy_parser.add_argument("script", help="Path to your Python agent script")

    sub.add_parser("status", help="List all registered agents")

    logs_parser = sub.add_parser("logs", help="Show logs for an agent")
    logs_parser.add_argument("name", help="Agent name")

    args = parser.parse_args()

    if args.command == "deploy":
        cmd_deploy(args.script)
    elif args.command == "status":
        cmd_status()
    elif args.command == "logs":
        cmd_logs(args.name)


if __name__ == "__main__":
    main()
