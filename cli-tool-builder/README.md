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
amplifier tool invoke recipes operation=execute recipe_path="@amplifier-expert-cookbook:cli-tool-builder/recipes/cli-tool-development.yaml" context='{"cli_description": "Build a CLI that..."}'
```

Or in an interactive session:

```bash
amplifier
```

Then:

```
Run the recipe at @amplifier-expert-cookbook:cli-tool-builder/recipes/cli-tool-development.yaml with cli_description: "Build a CLI that..."
```

**Note:** For subdirectory bundles, use the root bundle namespace (`@amplifier-expert-cookbook:`) with the full path from repo root, not the subdirectory bundle name.

## Development Stages

1. **Capability Reconnaissance** - Identify key challenges and explore multiple approaches
2. **Pilot Implementations** - Test each approach with rigorous test cases
3. **Production Building Blocks** - Build robust implementations of winning approaches
4. **Application Planning** - Design the final CLI architecture
5. **Implementation** - Build the complete application
6. **Testing** - Thorough testing and bug fixing

## Available Context

- `@amplifier-expert-cookbook:cli-tool-builder/context/uv-scripts.md` - Python scripting patterns with uv
- `@amplifier-expert-cookbook:cli-tool-builder/context/claude-agent-sdk.md` - Agentic solution patterns
