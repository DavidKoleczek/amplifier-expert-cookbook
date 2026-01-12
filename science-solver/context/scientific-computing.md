# Scientific Computing with Python and UV

When solving scientific problems, use `uv` for dependency management and script execution. This enables self-contained Python scripts with inline dependencies.

## Inline Script Dependencies

For standalone scientific scripts, declare dependencies directly in the file using PEP 723 inline metadata:

```python
# /// script
# dependencies = [
#   "sympy",
#   "numpy",
#   "scipy",
#   "pint",
# ]
# ///

import sympy as sp
import numpy as np

# Your scientific code here...
```

Run with: `uv run script.py`

uv automatically creates an isolated environment with the specified dependencies.
