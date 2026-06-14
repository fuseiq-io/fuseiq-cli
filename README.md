# fuseiq-cli

The official CLI for [FuseIQ](https://fuseiq.io) — deploy, manage, and
monitor your AI agents from the terminal.

## Install

```bash
pip install fuseiq-cli
```

## Usage

```bash
# Register a Python script as an agent
fuseiq deploy my_agent.py

# List all registered agents
fuseiq status

# View agent logs (opens dashboard link)
fuseiq logs my_agent
```

## What it does

- **`fuseiq deploy <script>`** — registers a Python script as a FuseIQ
  agent, saves metadata, and points you to the dashboard.
- **`fuseiq status`** — lists all registered agents with their status.
- **`fuseiq logs <name>`** — links to the live log view on fuseiq.io.

Full monitoring, real-time metrics, and alerting are available on the
FuseIQ dashboard at [https://fuseiq.io/dashboard](https://fuseiq.io/dashboard).

## Requirements

- Python 3.8+

## License

MIT
