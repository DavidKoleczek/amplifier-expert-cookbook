# CLI Tool Builder

An Amplifier bundle for building CLI applications through multi-stage development.

## Setup

```bash
amplifier bundle add git+https://github.com/DavidKoleczek/amplifier-expert-cookbook@main
amplifier bundle use cli-tool-builder
```

## Usage

**Interactive:**

```
Run the cli-tool-development recipe with cli_description: "Build a CLI tool that..."
```

**Non-Interactive:**

```bash
amplifier recipes execute cli-tool-builder:recipes/cli-tool-development.yaml \
  --context '{"cli_description": "Build a CLI tool that..."}'
```

## Process

The recipe executes 6 stages:

1. **Capability Recon** - Identify challenges, propose 3-5 diverse approaches per challenge, define test cases
2. **Pilot Implementations** - Implement and test each approach (5+ test cases each)
3. **Building Blocks** - Build production versions of winning approaches
4. **Planning** - Design CLI architecture using the building blocks
5. **Implementation** - Build the complete application
6. **Testing** - Comprehensive testing and bug fixes

## Context Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `cli_description` | Yes | - | Full description of the CLI tool to build |
| `project_dir` | No | `.` | Target directory for the project |
| `working_dir` | No | `.ai_working` | Directory for intermediate artifacts |

## Context Files

The bundle provides two context files to agents:

- **uv-scripts.md** - Python/uv patterns: inline dependencies (PEP 723), CLI frameworks (typer/click), modular project imports
- **claude-agent-sdk.md** - Agentic solutions using Claude Agent SDK: `query()`, `ClaudeSDKClient`, custom tools

## Structure

```
amplifier-expert-cookbook/
├── bundle.md
├── context/
│   ├── uv-scripts.md
│   └── claude-agent-sdk.md
└── recipes/
    └── cli-tool-development.yaml
```
