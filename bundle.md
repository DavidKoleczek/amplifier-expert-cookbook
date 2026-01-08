---
bundle:
  name: amplifier-expert-cookbook
  version: 0.1.0
  description: Expert examples and reusable workflows for Amplifier
---

# Amplifier Expert Cookbook

This repository contains multiple bundles. Use `#subdirectory=` to load specific ones:

- `cli-tool-builder` - Multi-stage CLI application development
- `arc-agi-solver` - ARC-AGI-2 task solver with parallel experts and voting

Example:
```
amplifier bundle add git+https://github.com/DavidKoleczek/amplifier-expert-cookbook@main#subdirectory=cli-tool-builder
amplifier bundle add git+https://github.com/DavidKoleczek/amplifier-expert-cookbook@main#subdirectory=arc-agi-solver
```
