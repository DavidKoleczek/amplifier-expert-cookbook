# CLI Tool Builder

Multi-stage CLI application development with capability reconnaissance and pilot implementations.

## Development Stages

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
cli-tool-builder/
├── bundle.md
├── context/
│   ├── uv-scripts.md
│   └── claude-agent-sdk.md
└── recipes/
    └── cli-tool-development.yaml
```

## Note on Subdirectory Bundles

For subdirectory bundles, use the root bundle namespace with the full path from repo root:

```
@amplifier-expert-cookbook:cli-tool-builder/recipes/cli-tool-development.yaml
```
