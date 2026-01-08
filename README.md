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

---

## ARC-AGI Solver

Solve [ARC-AGI-2](https://github.com/arcprize/ARC-AGI-2) tasks using iterative code synthesis with parallel experts and majority voting. Based on [Poetiq's ARC-AGI solver](https://github.com/poetiq-ai/poetiq-arc-agi-solver).

[Full documentation](./arc-agi-solver/)

### Setup

```bash
amplifier bundle add git+https://github.com/DavidKoleczek/amplifier-expert-cookbook@main#subdirectory=arc-agi-solver
amplifier bundle use arc-agi-solver
```

### Usage

**Interactive:**

```
Run the recipe at @amplifier-expert-cookbook:arc-agi-solver/recipes/arc-solver.yaml with task_file: "path/to/task.txt"
```

**Non-Interactive:**

```bash
amplifier recipes execute @amplifier-expert-cookbook:arc-agi-solver/recipes/arc-solver.yaml \
  --context '{"task_file": "path/to/task.txt"}'
```
