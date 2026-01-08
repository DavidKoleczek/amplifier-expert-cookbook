# Amplifier Expert Cookbook

Expert examples and reusable workflows for [Amplifier](https://github.com/microsoft/amplifier).

## CLI Tool Builder

Multi-stage CLI application development with capability reconnaissance and pilot implementations.

[Full documentation](./cli-tool-builder/)

### Setup

```bash
amplifier bundle add git+https://github.com/DavidKoleczek/amplifier-expert-cookbook@main#subdirectory=cli-tool-builder
amplifier bundle use cli-tool-builder
```

### Usage

**Interactive:**

```
Run the recipe at @amplifier-expert-cookbook:cli-tool-builder/recipes/cli-tool-development.yaml with cli_description: "Build a CLI tool that..."
```

**Non-Interactive:**

```bash
amplifier recipes execute @amplifier-expert-cookbook:cli-tool-builder/recipes/cli-tool-development.yaml \
  --context '{"cli_description": "Build a CLI tool that..."}'
```
