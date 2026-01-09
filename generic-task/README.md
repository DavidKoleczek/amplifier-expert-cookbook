# Generic Task Builder

General-purpose workflow for building software solutions using a streamlined 3-phase approach.

## When to Use

Use this for any non-trivial task:
- Building scripts or tools
- Creating automations
- Implementing features
- Prototyping solutions
- Any multi-step development work
- Research, analysis, writing, or planning tasks

For specialized tasks, consider:
- **ARC-AGI Solver** - For ARC-AGI puzzle solving specifically
- **CLI Tool Builder** - For comprehensive CLI apps requiring the full 6-stage process

## Phases

### Phase 1: Capability Recon & Plan
Identify what will be challenging about this task:
- External dependencies and APIs
- Complexity and nuanced decisions
- Integration challenges
- Edge cases to handle

Create an implementation plan with ordered steps.

### Phase 2: Build Modular Components / Create Plan

**For coding tasks:**
- Create focused, testable modules for each hard part
- Verify each works independently
- Document the API for integration
- Create a proposal for the final solution

**For non-coding tasks:**
- Create a detailed execution plan with validation criteria
- Break down into concrete, actionable steps
- Specify deliverables for each step

### Phase 3: Execute and Validate End-to-End

**For coding tasks:**
- Integrate all components
- Create entry point
- Test thoroughly
- Debug and fix any issues (don't give up!)
- Document usage

**For non-coding tasks:**
- Execute the plan step by step
- Validate against criteria
- Produce all deliverables
- Adapt if needed (don't give up!)

## Usage

### Standalone Bundle

```bash
amplifier bundle use generic-task
```

Then describe your task naturally.

### Via Meta-Bundle Router

```bash
amplifier bundle use amplifier-expert-cookbook
```

The router will automatically select this workflow for most non-trivial tasks.

### Direct Recipe Execution

```bash
amplifier run "execute @amplifier-expert-cookbook:generic-task/recipes/generic-task.yaml with task_description='Build a script that...'"
```

## Context Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `task_description` | Yes | - | Description of what you want to build |
| `project_dir` | No | `.` | Where to create the solution |
| `working_dir` | No | `.ai_working` | Directory for intermediate artifacts |

## Model Configuration

Uses Anthropic models only:
- `claude-haiku-4-5-20251001` - Fast, simple tasks
- `claude-sonnet-4-5-20250929` - All other tasks
