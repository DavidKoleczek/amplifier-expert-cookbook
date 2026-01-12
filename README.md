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
"Build me a script that fetches weather data"
"Create a tool that converts markdown to HTML"
"Solve the ARC task in ./puzzles/task_001.json"
```

Amplifier will automatically route to the appropriate specialized workflow.

---

## Available Workflows

| Workflow | Description | When to Use |
|----------|-------------|-------------|
| **Generic Task Builder** | Streamlined 3-phase development: recon, modular build, integration | **DEFAULT** - Most non-trivial tasks |
| **ARC-AGI Solver** | Parallel experts with majority voting for ARC puzzles | ARC-AGI benchmark tasks only |
| **CLI Tool Builder** | Comprehensive 6-stage CLI development | Full CLI apps with pilot implementations |
| **Science Problem Solver** | 4-stage scientific problem solving with code verification | Physics, chemistry, biology, math problems |

---

## Routing Logic

The meta-bundle automatically routes your requests:

1. **Trivial tasks** (questions, explanations) → Handled directly
2. **Non-trivial tasks** (building, coding) → **Generic Task Builder** (default)
3. **ARC-AGI puzzles** → ARC-AGI Solver
4. **Comprehensive CLI apps** → CLI Tool Builder (when explicitly requested)
5. **Scientific problems** → Science Problem Solver

---

## Workflows

### Generic Task Builder (DEFAULT)

Streamlined 3-phase approach for building software solutions. **This is the default for most tasks.**

**How it works:**
1. **Capability Recon & Plan**: Identify hard parts, explore approaches, create plan
2. **Build Modular Components**: Solve each challenge independently with testable modules
3. **Build & Test E2E**: Integrate, test, debug until working (doesn't give up!)

**Required context:**
- `task_description`: Description of what to build

**Optional context:**
- `project_dir`: Target directory (default: `.`)
- `working_dir`: Intermediate artifacts (default: `.ai_working`)

[Full documentation](./generic-task/)

---

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
- `max_iterations`: Max refinement attempts (default: `3`)

[Full documentation](./arc-agi-solver/)

---

### CLI Tool Builder

Comprehensive multi-stage CLI application development with capability reconnaissance and pilot implementations.

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

### Science Problem Solver

Systematic scientific problem solving for physics, chemistry, biology, and mathematics with staged verification and code validation.

**How it works:**
1. **Understand**: Parse problem, identify given information, what to find, and constraints
2. **Strategy**: Figure out approaches, plan for code verification
3. **Solve**: Execute step-by-step with feedback loop checking assumptions iteratively
4. **Verify**: Check answer using multiple verification methods, iterate if needed

**Required context:**
- `problem`: The scientific problem statement

**Optional context:**
- `output_dir`: Directory for intermediate files (default: `./solution_workspace`)
- `answer_file`: Specific path for final answer if required by problem

**Scientific computing:** The solver can use Python libraries via uv inline scripts (SymPy, NumPy, SciPy, Pint, etc.) for symbolic math, numerical computation, and unit handling.

**Standalone usage:**
```bash
# Use the science-solver bundle directly
amplifier bundle use amplifier-expert-cookbook:science-solver

# Or execute the recipe directly
amplifier run "execute @amplifier-expert-cookbook:science-solver/recipes/phd-problem-solver.yaml with problem='Calculate the partition function for a quantum harmonic oscillator at temperature T'"
```

[Full documentation](./science-solver/)

---

## Configuration

### Enabling/Disabling Workflows

Edit `context/workflows.yaml` to toggle workflows:

```yaml
workflows:
  - id: generic-task
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
   ├── context/         # Optional context files
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
