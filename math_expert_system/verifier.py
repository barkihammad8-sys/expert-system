"""Lightweight checks for solver results."""

import math
from typing import Any, Dict


def verify_result(operation: str, result: Dict[str, Any], parameters: Dict[str, Any]) -> Dict[str, Any]:
    """Return a transparent verification status; never claim a check was done if it was not."""
    if operation == "solve_equation" and "solutions" in result:
        try:
            import sympy
            x = sympy.Symbol("x")
            lhs = sympy.sympify(parameters["left"].replace("^", "**"))
            rhs = sympy.sympify(parameters["right"].replace("^", "**"))
            checks = [sympy.simplify((lhs - rhs).subs(x, value)) == 0 for value in result["solutions"]]
            return {"verified": all(checks), "details": "Substituted each reported solution into the original equation."}
        except Exception:
            return {"verified": None, "details": "Could not independently substitute the symbolic solutions."}
    if "numeric_answer" in result and math.isfinite(float(result["numeric_answer"])):
        return {"verified": True, "details": "Checked that the numeric result is finite."}
    if operation in ("differentiate", "integrate", "simplify"):
        return {"verified": None, "details": "Symbolic result returned; no independent proof check was performed."}
    return {"verified": None, "details": "No verification method is available for this result."}
