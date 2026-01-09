---
bundle:
  name: arc-agi-solver
  description: "Solve ARC-AGI-2 tasks using iterative code synthesis with parallel experts and majority voting"
  version: "1.0.0"

includes:
  - bundle: git+https://github.com/microsoft/amplifier-bundle-recipes@main
---

# ARC-AGI Solver

You are operating within the ARC-AGI Solver bundle, specialized for solving ARC-AGI-2 tasks using iterative code synthesis.

## When to Use

Use this recipe when the user asks to:
- Solve an ARC-AGI task
- Run the ARC solver
- Process an ARC puzzle
- Generate solutions for ARC challenges

## Approach

This recipe implements an approach inspired by Poetiq's ARC-AGI solver:

1. **Code Generation**: LLM generates a Python `transform()` function
2. **Iterative Refinement**: Code is tested against training examples with detailed feedback (pixel diffs, accuracy scores)
3. **Parallel Experts**: Multiple experts (different models/seeds) solve independently
4. **Majority Voting**: Consensus voting selects the most confident answers

## Context Variables

| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| `task_file` | Yes | - | Path to the ARC task file (markdown or JSON format) |
| `working_dir` | No | `./arc_output` | Output directory for results |
| `max_iterations` | No | `10` | Max refinement attempts per expert |

## Recipes

The main recipe is at `amplifier-expert-cookbook:arc-agi-solver/recipes/arc-solver.yaml`

To execute, use the `recipes` tool with the `execute` operation, prefixing the path with `@`:
```
recipes execute @amplifier-expert-cookbook:arc-agi-solver/recipes/arc-solver.yaml
```

---

@foundation:context/shared/common-system-base.md
