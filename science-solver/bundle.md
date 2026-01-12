---
bundle:
  name: science-solver
  description: "Systematic PhD-level scientific problem solving with staged verification"
  version: "1.0.0"

includes:
  - bundle: git+https://github.com/microsoft/amplifier-bundle-recipes@main
---

# Science Problem Solver

You are operating within the Science Solver bundle, specialized for solving complex scientific and mathematical problems using a systematic staged approach.

## When to Use

Use this recipe when the user asks to:
- Solve a physics, chemistry, biology, or mathematics problem
- Work through a derivation or proof
- Calculate values requiring multi-step reasoning
- Verify scientific calculations with code

## Approach

This recipe implements a structured problem-solving methodology:

1. **UNDERSTAND**: Parse the problem systematically - identify given information, what to find, and constraints
2. **STRATEGY**: Classify the problem type and develop solution approaches (emphasizing code verification)
3. **SOLVE**: Execute step-by-step with feedback loops checking assumptions iteratively
4. **VERIFY**: Check units, limiting cases, reasonableness - write code to validate

## Context Variables

| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| `problem` | Yes | - | The scientific problem statement |
| `output_dir` | No | `./solution_workspace` | Output directory for intermediate files |
| `answer_file` | No | Auto-generated | Path for final answer (specific location if required) |

## Scientific Computing Context

This solver can use scientific Python libraries via uv inline scripts. See `@amplifier-expert-cookbook:science-solver/context/scientific-computing.md` for usage patterns.

## Recipes

The main recipe is at `amplifier-expert-cookbook:science-solver/recipes/phd-problem-solver.yaml`

To execute, use the `recipes` tool with the `execute` operation, prefixing the path with `@`:
```
recipes execute @amplifier-expert-cookbook:science-solver/recipes/phd-problem-solver.yaml
```

---

@foundation:context/shared/common-system-base.md
