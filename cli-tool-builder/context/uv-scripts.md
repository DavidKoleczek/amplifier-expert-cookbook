# Python Development with UV

When building CLI tools, use `uv` for dependency management and script execution.

## Inline Script Dependencies

For standalone scripts, declare dependencies directly in the file using PEP 723 inline metadata:

```python
# /// script
# dependencies = [
#   "requests<3",
#   "rich",
# ]
# ///

import requests
from rich.pretty import pprint

resp = requests.get("https://peps.python.org/api/peps.json")
data = resp.json()
pprint([(k, v["title"]) for k, v in data.items()][:10])
```

Run with: `uv run example.py`

uv automatically creates an isolated environment with the specified dependencies.

## CLI Application Pattern

For full CLI applications, use `typer` or `click`:

```python
# /// script
# dependencies = [
#   "typer",
#   "rich",
# ]
# ///

import typer
from rich import print

app = typer.Typer()

@app.command()
def main(name: str, verbose: bool = False):
    """Greet the user."""
    if verbose:
        print(f"[bold green]Hello, {name}![/bold green]")
    else:
        print(f"Hello, {name}")

if __name__ == "__main__":
    app()
```

## Click Alternative

```python
# /// script
# dependencies = [
#   "click",
#   "rich",
# ]
# ///

import click
from rich import print

@click.command()
@click.argument("name")
@click.option("--verbose", "-v", is_flag=True, help="Enable verbose output")
def main(name: str, verbose: bool):
    """Greet the user."""
    if verbose:
        print(f"[bold green]Hello, {name}![/bold green]")
    else:
        print(f"Hello, {name}")

if __name__ == "__main__":
    main()
```

## Python Version Requirements

Specify Python version constraints:

```python
# /// script
# requires-python = ">=3.12"
# dependencies = ["httpx"]
# ///
```

## Running Scripts in Projects

When running in a directory with `pyproject.toml`, use `--no-project` to avoid installing project dependencies:

```bash
uv run --no-project example.py
```

## Modular Projects: Importing Local Files

For larger CLI tools, split code into multiple files. Local imports work automatically when running with `uv run`.

### Project Structure

```
my_cli/
├── cli.py              # Entry point with inline dependencies
├── api.py              # API client module
├── utils.py            # Utility functions
└── models.py           # Data models
```

### Entry Point (cli.py)

Only the entry point needs inline dependencies:

```python
# /// script
# dependencies = ["typer", "httpx", "rich"]
# ///

import typer
from api import fetch_data
from utils import format_output
from models import Result

app = typer.Typer()

@app.command()
def main(query: str):
    data = fetch_data(query)
    print(format_output(data))

if __name__ == "__main__":
    app()
```

### Local Module (api.py)

No inline metadata needed - dependencies come from the entry point:

```python
import httpx

def fetch_data(query: str) -> dict:
    response = httpx.get(f"https://api.example.com/search?q={query}")
    return response.json()
```

### Local Module (utils.py)

```python
from rich.table import Table
from rich.console import Console

def format_output(data: dict) -> str:
    console = Console()
    table = Table(title="Results")
    # ... format data
    return table
```

### Running

```bash
cd my_cli
uv run cli.py "search term"
```

### Key Points for Modular Projects

1. **Only the entry point** needs `# /// script` metadata
2. **Local imports** work naturally - Python finds sibling files
3. **Run from the project directory** so imports resolve correctly
4. **Shared dependencies** are declared once in the entry point

### Relative Imports (for packages)

If you structure as a proper package with `__init__.py`:

```
my_cli/
├── __init__.py
├── __main__.py         # Entry point
├── api.py
└── utils.py
```

Use relative imports:

```python
# __main__.py
from .api import fetch_data
from .utils import format_output
```

Run as a module:

```bash
uv run -m my_cli "search term"
```

## Key Points

1. **Inline metadata** keeps scripts self-contained and portable
2. **uv handles environments** - no manual venv management needed
3. **Dependencies are cached** - subsequent runs are fast
4. **Version constraints** work just like requirements.txt
5. **Local imports** work automatically for modular projects
