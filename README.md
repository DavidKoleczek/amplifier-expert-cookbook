# Amplifier Expert Cookbook

Expert examples and reusable bundles for [Amplifier](https://github.com/microsoft/amplifier) leveraging [recipes](https://github.com/microsoft/amplifier-bundle-recipes).

## Quick Start

```bash
# Install the meta-bundle (router mode)
amplifier bundle add git+https://github.com/DavidKoleczek/amplifier-expert-cookbook@main
amplifier bundle use amplifier-expert-cookbook
```

Then just describe what you want:

```
"Solve the ARC task in ./puzzles/task_001.json"
"Build me a CLI tool that fetches weather data"
```

Amplifier will automatically route to the appropriate specialized workflow.

---

## Available Workflows

| Workflow | Description |
|----------|-------------|
| **ARC-AGI Solver** | Solve ARC-AGI-2 tasks with parallel experts and voting |
| **CLI Tool Builder** | Multi-stage CLI development with recon and pilots |

---

## Usage

Load the meta-bundle and let the AI route your requests:

```bash
amplifier bundle use amplifier-expert-cookbook
```

**Interactive:**
```
User: "I need to solve the ARC task in tasks/puzzle.json"
Amplifier: Routes to ARC-AGI Solver automatically
```

---

## Workflows

### ARC-AGI Solver

Solve [ARC-AGI-2](https://github.com/arcprize/ARC-AGI-2) tasks using iterative code synthesis with parallel experts and majority voting.

**How it works:**
1. Multiple experts (different models) generate `transform()` functions
2. Code is tested against training examples with detailed feedback
3. Experts iterate until tests pass or max iterations reached
4. Majority voting selects the best answer

**Required context:**
- `task_file`: Path to the ARC task file (markdown or JSON)

**Optional context:**
- `working_dir`: Output directory (default: `./arc_output`)
- `max_iterations`: Max refinement attempts (default: `10`)

[Full documentation](./arc-agi-solver/)

---

### CLI Tool Builder

Multi-stage CLI application development with capability reconnaissance and pilot implementations.

**How it works:**
1. **Capability Recon**: Identify key challenges, explore diverse approaches
2. **Pilot Implementations**: Test each approach with rigorous test cases
3. **Production Blocks**: Build robust implementations of winning approaches
4. **Application Planning**: Design the final CLI architecture
5. **Implementation**: Build the complete application
6. **Testing**: Thorough testing and bug fixing

**Required context:**
- `cli_description`: Description of the CLI tool to build

**Optional context:**
- `project_dir`: Target directory (default: `.`)
- `working_dir`: Intermediate artifacts (default: `.ai_working`)

[Full documentation](./cli-tool-builder/)

---

## Configuration

### Enabling/Disabling Workflows

Edit `context/workflows.yaml` to toggle workflows:

```yaml
workflows:
  - id: arc-agi
    enabled: false  # Disabled - won't be routed to automatically
    # ...
```

Disabled workflows are still accessible via direct recipe invocation.

### Adding New Workflows

1. Create a subdirectory with your workflow:
   ```
   my-workflow/
   ├── bundle.md        # For standalone use
   ├── README.md
   └── recipes/
       └── my-recipe.yaml
   ```

2. Add an entry to `context/workflows.yaml`:
   ```yaml
   - id: my-workflow
     name: "My Workflow"
     enabled: true
     description: >
       Clear description of what this workflow does and when to use it.
       The AI uses this to determine if a user's request matches.
     recipe: "@amplifier-expert-cookbook:my-workflow/recipes/my-recipe.yaml"
     context:
       required:
         - name: input_var
           description: "What this variable is for"
       optional:
         - name: optional_var
           default: "default_value"
   ```


