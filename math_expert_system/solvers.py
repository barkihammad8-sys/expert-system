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


def _decimal(value, sympy, digits=10):
    """Return a readable decimal approximation, including complex values."""
    return str(sympy.N(value, digits))


def solve_equation(left: str, right: str) -> Dict[str, Any]:
    sympy, lhs = _parse(left)
    _, rhs = _parse(right)
    x = sympy.Symbol("x")
    equation_expression = sympy.expand(lhs - rhs)
    solutions = sympy.solve(sympy.Eq(lhs, rhs), x)
    if not solutions:
        return {
            "answer": "No solution",
            "latex_answer": r"\text{No solution}",
            "explanation": f"Set {left} equal to {right} and solve for x.",
        }

    display_solutions = []
    decimal_solutions = []
    latex_solutions = []
    try:
        degree = sympy.Poly(equation_expression, x).degree()
    except (sympy.polys.polyerrors.PolynomialError, TypeError):
        degree = None

    for value in solutions:
        exact = sympy.simplify(value)
        display_solutions.append(f"x = {exact}")
        decimal_solutions.append(f"x ≈ {_decimal(value, sympy, 10)}")
        latex_solutions.append("x = " + sympy.latex(exact))

    degree_note = " This is a cubic equation; all solutions returned by the symbolic solver are listed." if degree == 3 else ""
    return {
        "answer": "; ".join(display_solutions),
        "latex_answer": r",\quad ".join(latex_solutions),
        "numeric_answer": "; ".join(decimal_solutions),
        "solutions": solutions,
        "explanation": f"Rearrange the equation {left} = {right}, then solve it for x.{degree_note}",
    }


def differentiate(expression: str, variable: str = "x") -> Dict[str, Any]:
    sympy, expr = _parse(expression)
    symbol = sympy.Symbol(variable)
    result = sympy.diff(expr, symbol)
    return {
        "answer": str(result),
        "latex_answer": sympy.latex(result),
        "explanation": f"Differentiate {expression} with respect to {variable} using the power and derivative rules.",
    }


def integrate(expression: str, variable: str = "x") -> Dict[str, Any]:
    sympy, expr = _parse(expression)
    symbol = sympy.Symbol(variable)
    result = sympy.integrate(expr, symbol)
    answer = f"{result} + C"
    return {
        "answer": answer,
        "latex_answer": sympy.latex(result) + r" + C",
        "explanation": f"Find an antiderivative of {expression} with respect to {variable}. C is the constant of integration.",
    }


def simplify(expression: str) -> Dict[str, Any]:
    sympy, expr = _parse(expression)
    result = sympy.simplify(expr)
    return {
        "answer": str(result),
        "latex_answer": sympy.latex(result),
        "explanation": f"SymPy simplified the expression {expression}.",
    }


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
    return {
        "answer": f"{result:.12g}",
        "numeric_answer": result,
        "latex_answer": f"{result:.12g}",
        "formula": formula,
        "explanation": f"Substitute the given measurements into {formula}.",
    }


def solve_trig(function: str, angle: float) -> Dict[str, Any]:
    radians = math.radians(angle)
    functions = {"sin": math.sin, "cos": math.cos, "tan": math.tan}
    if function not in functions:
        raise ValueError("Supported trigonometric functions are sin, cos, and tan.")
    if function == "tan" and math.isclose(math.cos(radians), 0.0, abs_tol=1e-12):
        raise ValueError("Tangent is undefined for this angle.")
    result = functions[function](radians)
    if math.isclose(result, 0.0, abs_tol=1e-12):
        result = 0.0
    elif math.isclose(result, 1.0, abs_tol=1e-12):
        result = 1.0
    elif math.isclose(result, -1.0, abs_tol=1e-12):
        result = -1.0
    return {
        "answer": f"{result:.8g}",
        "numeric_answer": result,
        "latex_answer": f"{result:.8g}",
        "formula": f"{function}({angle}°)",
        "explanation": "Convert the angle from degrees to radians, then evaluate the trigonometric function.",
    }
