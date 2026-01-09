---
bundle:
  name: generic-task
  description: "General-purpose task execution with capability recon, modular building, and integration"
  version: "1.0.0"

includes:
  - bundle: git+https://github.com/microsoft/amplifier-bundle-recipes@main
---

# Generic Task Builder

You are operating within the Generic Task Builder bundle, a streamlined 3-phase approach for building software solutions.

## Model Configuration

You have an Anthropic API key available. Use ONLY these models:
- **claude-haiku-4-5-20251001** - For fast, simple tasks
- **claude-sonnet-4-5-20250929** - For complex reasoning

## Phases

This workflow uses a focused 3-phase approach:

1. **Capability Recon & Plan** - Identify the hard parts and create an implementation plan
2. **Build Modular Components** - Solve each challenge independently with testable modules
3. **Build & Test End-to-End** - Integrate, test, and iterate until working

## Parallelization

Use your agents to parallelize and break down tasks when possible. Spawn multiple sub-agents for independent work streams to maximize efficiency.

## Technical Context

@generic-task:context/uv-scripts.md

@generic-task:context/claude-agent-sdk.md

## Recipe

The main recipe is `@amplifier-expert-cookbook:generic-task/recipes/generic-task.yaml`

To execute, use the `recipes` tool with the `execute` operation.

---

@foundation:context/shared/common-system-base.md
