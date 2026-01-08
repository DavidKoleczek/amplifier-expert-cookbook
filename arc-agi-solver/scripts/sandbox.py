#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "numpy",
# ]
# ///
"""
ARC-AGI Code Sandbox

Executes transform() code against input grids and validates outputs.
Provides detailed feedback including pixel diffs, shape mismatches, and accuracy scores.

Usage:
    uv run sandbox.py --code-file=transform.py --task-file=task.json
    uv run sandbox.py --code="def transform(grid): return grid" --task-file=task.json
"""

import argparse
import json
import sys
import tempfile
import textwrap
import subprocess
import os
from typing import Optional
import re


def parse_task_from_markdown(content: str) -> dict:
    """Parse the ARC task from markdown format."""
    task = {"train": [], "test": []}
    
    # Find training examples
    example_pattern = r"### Example (\d+)\s*\nInput:\s*\n(\[\[.*?\]\])\s*\nOutput:\s*\n(\[\[.*?\]\])"
    for match in re.finditer(example_pattern, content, re.DOTALL):
        input_grid = json.loads(match.group(2))
        output_grid = json.loads(match.group(3))
        task["train"].append({"input": input_grid, "output": output_grid})
    
    # Find test inputs
    test_pattern = r"### Test (\d+)\s*\nInput:\s*\n(\[\[.*?\]\])"
    for match in re.finditer(test_pattern, content, re.DOTALL):
        input_grid = json.loads(match.group(2))
        task["test"].append({"input": input_grid})
    
    return task


def run_code(code: str, input_grid: list, timeout_s: float = 5.0) -> tuple[bool, str]:
    """Run transform code in a subprocess, returning (success, result_or_error)."""
    script = f"""
import json
import numpy as np
import sys

# User code
{code}

if __name__ == '__main__':
    data = json.load(sys.stdin)
    try:
        result = transform(np.array(data['input']))
        print(json.dumps({{"ok": True, "result": result.tolist()}}))
    except Exception as e:
        print(json.dumps({{"ok": False, "error": str(e)}}))
"""
    
    with tempfile.TemporaryDirectory() as td:
        path = os.path.join(td, "transform_script.py")
        with open(path, "w", encoding="utf-8") as f:
            f.write(textwrap.dedent(script))
        
        try:
            result = subprocess.run(
                [sys.executable, path],
                input=json.dumps({"input": input_grid}).encode(),
                capture_output=True,
                timeout=timeout_s,
                cwd=td,
                env={**os.environ, "PYTHONHASHSEED": "0"}
            )
        except subprocess.TimeoutExpired:
            return False, "TIMEOUT: Code execution exceeded time limit"
        
        if result.returncode != 0:
            error = result.stderr.decode() or result.stdout.decode()
            return False, f"EXECUTION ERROR:\n{error.strip()}"
        
        try:
            payload = json.loads(result.stdout.decode())
            if payload.get("ok"):
                return True, json.dumps(payload.get("result"))
            else:
                return False, f"RUNTIME ERROR: {payload.get('error', 'Unknown error')}"
        except json.JSONDecodeError as e:
            return False, f"OUTPUT PARSE ERROR: {e}"


def array_diff(pred: list, truth: list) -> str:
    """Create a visual diff showing prediction/correct for mismatched cells."""
    if len(pred) != len(truth) or (pred and len(pred[0]) != len(truth[0])):
        return f"Shape mismatch: predicted {len(pred)}x{len(pred[0]) if pred else 0}, expected {len(truth)}x{len(truth[0]) if truth else 0}"
    
    lines = []
    for i, (pred_row, truth_row) in enumerate(zip(pred, truth)):
        row_parts = []
        for j, (p, t) in enumerate(zip(pred_row, truth_row)):
            if p == t:
                row_parts.append(str(p))
            else:
                row_parts.append(f"{p}/{t}")
        lines.append(" ".join(row_parts))
    return "\n".join(lines)


def soft_score(pred: list, truth: list) -> float:
    """Calculate percentage of correctly predicted cells."""
    if not pred or not truth:
        return 0.0
    if len(pred) != len(truth) or len(pred[0]) != len(truth[0]):
        return 0.0
    
    total = 0
    correct = 0
    for pred_row, truth_row in zip(pred, truth):
        for p, t in zip(pred_row, truth_row):
            total += 1
            if p == t:
                correct += 1
    
    return correct / total if total > 0 else 0.0


def evaluate_code(code: str, task: dict, timeout_s: float = 5.0) -> dict:
    """
    Evaluate transform code against all training examples.
    Returns detailed results with feedback.
    """
    results = {
        "all_passed": True,
        "train_results": [],
        "test_results": [],
        "total_score": 0.0,
        "feedback": ""
    }
    
    feedback_parts = []
    scores = []
    
    # Evaluate on training examples
    for i, example in enumerate(task["train"]):
        input_grid = example["input"]
        expected_output = example["output"]
        
        success, output = run_code(code, input_grid, timeout_s)
        
        example_result = {
            "example_num": i + 1,
            "success": False,
            "score": 0.0,
            "feedback": ""
        }
        
        if not success:
            results["all_passed"] = False
            example_result["feedback"] = f"Example #{i+1} FAILED:\n{output}"
            example_result["score"] = 0.0
            feedback_parts.append(example_result["feedback"])
        else:
            try:
                pred_grid = json.loads(output)
                
                # Check exact match
                if pred_grid == expected_output:
                    example_result["success"] = True
                    example_result["score"] = 1.0
                    example_result["feedback"] = f"Example #{i+1} PASSED"
                    feedback_parts.append(example_result["feedback"])
                else:
                    results["all_passed"] = False
                    score = soft_score(pred_grid, expected_output)
                    example_result["score"] = score
                    
                    # Build detailed feedback
                    fb_lines = [f"Example #{i+1} INCORRECT:"]
                    
                    # Shape check
                    pred_shape = (len(pred_grid), len(pred_grid[0]) if pred_grid else 0)
                    exp_shape = (len(expected_output), len(expected_output[0]) if expected_output else 0)
                    
                    if pred_shape != exp_shape:
                        fb_lines.append(f"  Shape mismatch: predicted {pred_shape}, expected {exp_shape}")
                    else:
                        fb_lines.append(f"  Accuracy: {score*100:.1f}% of pixels correct")
                        fb_lines.append("  Diff (predicted/expected for wrong cells):")
                        diff = array_diff(pred_grid, expected_output)
                        for line in diff.split("\n"):
                            fb_lines.append(f"    {line}")
                    
                    example_result["feedback"] = "\n".join(fb_lines)
                    feedback_parts.append(example_result["feedback"])
                    
            except (json.JSONDecodeError, TypeError) as e:
                results["all_passed"] = False
                example_result["feedback"] = f"Example #{i+1} OUTPUT PARSE ERROR: {e}"
                feedback_parts.append(example_result["feedback"])
        
        scores.append(example_result["score"])
        results["train_results"].append(example_result)
    
    # Run on test inputs (no validation, just get outputs)
    for i, test in enumerate(task.get("test", [])):
        input_grid = test["input"]
        success, output = run_code(code, input_grid, timeout_s)
        
        test_result = {
            "test_num": i,
            "success": success,
            "output": None,
            "error": None
        }
        
        if success:
            try:
                test_result["output"] = json.loads(output)
            except json.JSONDecodeError:
                test_result["success"] = False
                test_result["error"] = "Failed to parse output"
        else:
            test_result["error"] = output
        
        results["test_results"].append(test_result)
    
    results["total_score"] = sum(scores) / len(scores) if scores else 0.0
    results["feedback"] = "\n\n".join(feedback_parts)
    
    return results


def main():
    parser = argparse.ArgumentParser(description="ARC-AGI Code Sandbox")
    parser.add_argument("--code-file", help="Path to file containing transform code")
    parser.add_argument("--code", help="Transform code as string")
    parser.add_argument("--task-file", required=True, help="Path to task file (JSON or markdown)")
    parser.add_argument("--timeout", type=float, default=5.0, help="Execution timeout in seconds")
    parser.add_argument("--output", choices=["json", "text"], default="json", help="Output format")
    
    args = parser.parse_args()
    
    # Load code
    if args.code_file:
        with open(args.code_file, "r") as f:
            code = f.read()
    elif args.code:
        code = args.code
    else:
        print("Error: Must provide --code-file or --code", file=sys.stderr)
        sys.exit(1)
    
    # Load task
    with open(args.task_file, "r") as f:
        content = f.read()
    
    # Detect format (JSON or markdown)
    try:
        task = json.loads(content)
    except json.JSONDecodeError:
        task = parse_task_from_markdown(content)
    
    if not task["train"]:
        print("Error: No training examples found in task file", file=sys.stderr)
        sys.exit(1)
    
    # Evaluate
    results = evaluate_code(code, task, args.timeout)
    
    # Output
    if args.output == "json":
        print(json.dumps(results, indent=2))
    else:
        print(f"All Passed: {results['all_passed']}")
        print(f"Score: {results['total_score']*100:.1f}%")
        print()
        print("=== Feedback ===")
        print(results["feedback"])
        if results["test_results"]:
            print()
            print("=== Test Outputs ===")
            for tr in results["test_results"]:
                if tr["success"]:
                    print(f"Test {tr['test_num']}: {json.dumps(tr['output'])}")
                else:
                    print(f"Test {tr['test_num']}: ERROR - {tr['error']}")
    
    # Exit with status
    sys.exit(0 if results["all_passed"] else 1)


if __name__ == "__main__":
    main()
