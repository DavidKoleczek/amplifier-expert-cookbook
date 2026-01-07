# CLI Tool Builder

An Amplifier bundle for building CLI applications through multi-stage development.

## Installation

```bash
amplifier bundle add git+https://github.com/DavidKoleczek/amplifier-expert-cookbook@main#subdirectory=cli-tool-builder
amplifier bundle use cli-tool-builder
```

## Usage

Run the main recipe:

```bash
amplifier tool invoke recipes operation=execute recipe_path="@cli-tool-builder:recipes/cli-tool-development.yaml" context='{"cli_description": "Build a CLI that..."}'
```

Or in a session:

```
Run the cli-tool-development recipe with cli_description: "Build a CLI that..."
```

## Development Stages

1. **Capability Reconnaissance** - Identify key challenges and explore multiple approaches
2. **Pilot Implementations** - Test each approach with rigorous test cases
3. **Production Building Blocks** - Build robust implementations of winning approaches
4. **Application Planning** - Design the final CLI architecture
5. **Implementation** - Build the complete application
6. **Testing** - Thorough testing and bug fixing

## Available Context

- `@cli-tool-builder:context/uv-scripts.md` - Python scripting patterns with uv
- `@cli-tool-builder:context/claude-agent-sdk.md` - Agentic solution patterns
