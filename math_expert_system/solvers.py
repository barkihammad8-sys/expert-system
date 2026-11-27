"""Mathematical solvers used by the expert system."""

import math
import re
from typing import Any, Dict


_ALLOWED_EXPRESSION = re.compile(r"^[0-9A-Za-z_+\-*/().,\s^]+$")


def parse_expression(expression: str):
    """Parse a restricted arithmetic expression without exposing Python builtins."""
    if not expression or not _ALLOWED_EXPRESSION.fullmatch(expression):
        raise ValueError("Expression contains unsupported characters.")
    if "__" in expression:
        raise ValueError("Double underscores are not allowed in expressions.")
    try:
        import sympy
        from sympy.parsing.sympy_parser import (
            convert_xor,
            implicit_multiplication_application,
            parse_expr,
            standard_transformations,
        )
    except ImportError as exc:
        raise RuntimeError("SymPy is required for algebra and calculus. Run: pip install -r requirements.txt") from exc

    # Keep eval's global namespace deliberately small. Only arithmetic
    # constructors are available; Python builtins and attribute access are not.
    global_dict = {
        "__builtins__": {},
        "Symbol": sympy.Symbol,
        "Integer": sympy.Integer,
        "Float": sympy.Float,
        "Rational": sympy.Rational,
        "Add": sympy.Add,
        "Mul": sympy.Mul,
        "Pow": sympy.Pow,
    }
    local_dict = {
        name: sympy.Symbol(name) for name in ("x", "y", "z", "t", "a", "b", "c")
    }
    local_dict.update({
        "pi": sympy.pi,
        "E": sympy.E,
        "sqrt": sympy.sqrt,
        "sin": sympy.sin,
        "cos": sympy.cos,
        "tan": sympy.tan,
        "log": sympy.log,
        "exp": sympy.exp,
        "abs": sympy.Abs,
    })
    transformations = standard_transformations + (
        implicit_multiplication_application,
        convert_xor,
    )
    try:
        return sympy, parse_expr(
            expression,
            local_dict=local_dict,
            global_dict=global_dict,
            transformations=transformations,
            evaluate=True,
        )
    except (SyntaxError, TypeError, ValueError, NameError) as exc:
        raise ValueError(f"Invalid mathematical expression: {expression}") from exc


def _parse(expression: str):
    return parse_expression(expression)


def solve_equation(left: str, right: str) -> Dict[str, Any]:
    sympy, lhs = _parse(left)
    _, rhs = _parse(right)
    x = sympy.Symbol("x")
    solutions = sympy.solve(sympy.Eq(lhs, rhs), x)
    if not solutions:
        return {"answer": "No solution found for x.", "explanation": f"Set {left} equal to {right} and solve for x."}
    return {
        "answer": ", ".join(f"x = {sympy.simplify(value)}" for value in solutions),
        "solutions": solutions,
        "explanation": f"Rearrange the equation {left} = {right}, then solve it for x.",
    }


def differentiate(expression: str, variable: str = "x") -> Dict[str, Any]:
    sympy, expr = _parse(expression)
    symbol = sympy.Symbol(variable)
    result = sympy.diff(expr, symbol)
    return {"answer": str(result), "explanation": f"Differentiate {expression} with respect to {variable} using the power and derivative rules."}


def integrate(expression: str, variable: str = "x") -> Dict[str, Any]:
    sympy, expr = _parse(expression)
    symbol = sympy.Symbol(variable)
    result = sympy.integrate(expr, symbol)
    return {"answer": f"{result} + C", "explanation": f"Find an antiderivative of {expression} with respect to {variable}. C is the constant of integration."}


def simplify(expression: str) -> Dict[str, Any]:
    sympy, expr = _parse(expression)
    result = sympy.simplify(expr)
    return {"answer": str(result), "explanation": f"SymPy simplified the expression {expression}."}


def solve_geometry(operation: str, values: Dict[str, float]) -> Dict[str, Any]:
    if operation in ("circle_area", "circumference"):
        radius = values["radius"]
        if radius < 0:
            raise ValueError("Radius cannot be negative.")
        if operation == "circle_area":
            result, formula = math.pi * radius ** 2, "A = πr²"
        else:
            result, formula = 2 * math.pi * radius, "C = 2πr"
    elif operation in ("rectangle_area", "rectangle_perimeter"):
        length, width = values["length"], values["width"]
        if length < 0 or width < 0:
            raise ValueError("Length and width cannot be negative.")
        if operation == "rectangle_area":
            result, formula = length * width, "A = length × width"
        else:
            result, formula = 2 * (length + width), "P = 2(length + width)"
    elif operation == "triangle_area":
        base, height = values["base"], values["height"]
        if base < 0 or height < 0:
            raise ValueError("Base and height cannot be negative.")
        result, formula = 0.5 * base * height, "A = ½ × base × height"
    else:
        raise ValueError(f"Unknown geometry operation: {operation}")
    return {"answer": f"{result:.12g}", "numeric_answer": result, "formula": formula, "explanation": f"Substitute the given measurements into {formula}."}


def solve_trig(function: str, angle: float) -> Dict[str, Any]:
    radians = math.radians(angle)
    functions = {"sin": math.sin, "cos": math.cos, "tan": math.tan}
    if function not in functions:
        raise ValueError("Supported trigonometric functions are sin, cos, and tan.")
    if function == "tan" and math.isclose(math.cos(radians), 0.0, abs_tol=1e-12):
        raise ValueError("Tangent is undefined for this angle.")
    result = functions[function](radians)
    return {"answer": f"{result:.8g}", "numeric_answer": result, "formula": f"{function}({angle}°)", "explanation": "Convert the angle from degrees to radians, then evaluate the trigonometric function."}
