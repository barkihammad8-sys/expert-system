"""Natural-language parser for the question patterns supported by the project."""

import re
from typing import Any, Dict


def _number(text: str) -> float:
    return float(text)


def parse_question(question: str) -> Dict[str, Any]:
    """Convert a supported question into a structured operation.

    The parser intentionally accepts a documented set of patterns. It does not
    pretend to understand arbitrary conversational language.
    """
    text = question.strip().lower().replace("−", "-").replace("^", "**")
    if not text:
        raise ValueError("Please enter a mathematics question.")

    # Symbolic differentiation and integration.
    match = re.search(r"(?:differentiate|derivative\s+of)\s+(.+)", text)
    if match:
        return {"operation": "differentiate", "expression": match.group(1).strip(), "variable": "x"}
    match = re.search(r"(?:integrate|integral\s+of|antiderivative\s+of)\s+(.+)", text)
    if match:
        return {"operation": "integrate", "expression": match.group(1).strip(), "variable": "x"}

    # Trigonometry, with angles interpreted in degrees.
    match = re.search(r"\b(sin|sine|cos|cosine|tan|tangent)\s*(?:of\s*)?(-?\d+(?:\.\d+)?)", text)
    if match:
        name = match.group(1)
        operation = {"sine": "sin", "cosine": "cos", "tangent": "tan"}.get(name, name)
        return {"operation": "trig", "function": operation, "angle": _number(match.group(2))}

    # Circle measurements.
    radius = re.search(r"radius\s*(?:=|of)?\s*(-?\d+(?:\.\d+)?)", text)
    if radius and "circle" in text:
        operation = "circumference" if "circumference" in text or "perimeter" in text else "circle_area"
        return {"operation": operation, "radius": _number(radius.group(1))}

    # Rectangle measurements.
    if "rectangle" in text:
        length = re.search(r"length\s*(?:=|of)?\s*(-?\d+(?:\.\d+)?)", text)
        width = re.search(r"width\s*(?:=|of)?\s*(-?\d+(?:\.\d+)?)", text)
        if length and width:
            operation = "rectangle_perimeter" if "perimeter" in text else "rectangle_area"
            return {"operation": operation, "length": _number(length.group(1)), "width": _number(width.group(1))}

    # Triangle area.
    if "triangle" in text:
        base = re.search(r"base\s*(?:=|of)?\s*(-?\d+(?:\.\d+)?)", text)
        height = re.search(r"height\s*(?:=|of)?\s*(-?\d+(?:\.\d+)?)", text)
        if base and height:
            return {"operation": "triangle_area", "base": _number(base.group(1)), "height": _number(height.group(1))}

    # Equations: solve 2*x + 3 = 7, or solve x**2 - 5*x + 6 = 0.
    equation = re.search(r"(?:solve\s+)?(.+?)\s*=\s*(.+)", text)
    if equation:
        return {"operation": "solve_equation", "left": equation.group(1).strip(), "right": equation.group(2).strip()}

    # Symbolic simplification.
    expression = re.search(r"(?:simplify|simplification\s+of)\s+(.+)", text)
    if expression:
        return {"operation": "simplify", "expression": expression.group(1).strip()}

    raise ValueError(
        "I could not understand that question. Type 'help' to see supported examples."
    )
