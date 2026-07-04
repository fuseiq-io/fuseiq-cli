# FuseIQ CLI — Deploy and monitor agents from the terminal

[![PyPI](https://img.shields.io/pypi/v/fuseiq-cli)](https://pypi.org/project/fuseiq-cli/)
[![FuseIQ](https://img.shields.io/badge/FuseIQ-Outcome_OS-00D4FF?style=for-the-badge)](https://fuseiq.io)
[![Agent SDK](https://img.shields.io/badge/Agent_SDK-181717?style=for-the-badge&logo=github)](https://github.com/fuseiq-io/fuseiq-agent-sdk)

The official CLI for [FuseIQ](https://fuseiq.io) — deploy, manage, and
monitor your AI agents from the terminal.

> ⭐ Pair with [fuseiq-agent-sdk](https://github.com/fuseiq-io/fuseiq-agent-sdk) — star both repos for release alerts. PRs welcome for deploy recipes and CI hooks.

> **FuseIQ v2.2.6** — Pair the CLI with hosted Swarm Canvas, Library playbooks, and 157+ integrations. [Sign up free →](https://fuseiq.io/signup)

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

Full monitoring, real-time metrics, Swarm orchestration, and approval gates are available on the
FuseIQ dashboard at [https://fuseiq.io/dashboard](https://fuseiq.io/dashboard).

## Ecosystem

| Repo | Purpose |
|------|---------|
| [fuseiq-agent-sdk](https://github.com/fuseiq-io/fuseiq-agent-sdk) | Python + Node SDK |
| [fuseiq-templates](https://github.com/fuseiq-io/fuseiq-templates) | Example agents |
| **fuseiq-cli** (this repo) | Terminal tooling |

- Docs: [fuseiq.io/docs](https://fuseiq.io/docs)
- Help: [fuseiq.io/help](https://fuseiq.io/help)

## Requirements

- Python 3.8+

## License

MIT

---

⭐ **Star this repo** — help developers discover FuseIQ.