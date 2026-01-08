# CLI Tool Builder

An Amplifier bundle for building CLI applications through multi-stage development.

## Installation

```bash
amplifier bundle add git+https://github.com/DavidKoleczek/amplifier-expert-cookbook@main#subdirectory=cli-tool-builder
amplifier bundle use cli-tool-builder
```

## Usage

**Interactive:**
```
amplifier run
> Run the cli-tool-development recipe with cli_description: "Build a CLI tool that..."
```

**Non-Interactive:**
```bash
amplifier recipes execute cli-tool-builder:recipes/cli-tool-development.yaml \
  --context '{"cli_description": "Build a CLI tool that..."}'
```

## Context Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `cli_description` | Yes | - | Full description of the CLI tool to build |
| `project_dir` | No | `.` | Target directory for the project |
| `working_dir` | No | `.ai_working` | Directory for intermediate artifacts |

## Development Stages

The recipe executes 6 stages:

1. **Capability Reconnaissance** - Identify key challenges and propose 3-5 diverse approaches per challenge with test cases
2. **Pilot Implementations** - Implement and test each approach (5+ test cases each), document which works best
3. **Production Building Blocks** - Build robust implementations of winning approaches with clean APIs
4. **Application Planning** - Design CLI architecture, file structure, and implementation steps
5. **Implementation** - Build the complete application with entry point and error handling
6. **Testing** - Comprehensive functional, integration, and edge case testing

## Context Files

The bundle provides two context files to agents:

- **uv-scripts.md** - Python/uv patterns: inline dependencies (PEP 723), CLI frameworks (typer/click), modular project imports
- **claude-agent-sdk.md** - Agentic solutions using Claude Agent SDK for intelligent features and fallback strategies

## Structure

```
cli-tool-builder/
├── bundle.md               # Bundle configuration and agent instructions
├── README.md               # This file
├── context/
│   ├── uv-scripts.md       # Python scripting patterns
│   └── claude-agent-sdk.md # Agentic solution patterns
└── recipes/
    └── cli-tool-development.yaml  # 6-stage development workflow
```
