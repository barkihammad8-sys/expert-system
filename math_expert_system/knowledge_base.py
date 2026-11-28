"""Knowledge base containing the expert system's mathematical rules."""

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class Rule:
    """A simple production rule used by the expert system."""

    rule_id: str
    topic: str
    keywords: Tuple[str, ...]
    description: str


RULES = (
    Rule("ALG-LINEAR", "algebra", ("solve", "equation", "linear"), "Solve a one-variable linear equation."),
    Rule("ALG-QUADRATIC", "algebra", ("quadratic", "x^2", "x**2"), "Solve a quadratic equation."),
    Rule("ALG-CUBIC", "algebra", ("cubic", "x^3", "x**3", "degree 3"), "Solve a cubic equation (degree three)."),
    Rule("CAL-DIFF", "calculus", ("differentiate", "derivative"), "Differentiate an expression symbolically."),
    Rule("CAL-INTEGRATE", "calculus", ("integrate", "integral", "antiderivative"), "Integrate an expression symbolically."),
    Rule("GEO-CIRCLE", "geometry", ("circle", "radius"), "Calculate circle area or circumference."),
    Rule("GEO-RECTANGLE", "geometry", ("rectangle", "length", "width"), "Calculate rectangle area or perimeter."),
    Rule("GEO-TRIANGLE", "geometry", ("triangle", "base", "height"), "Calculate triangle area."),
    Rule("TRIG", "trigonometry", ("sin", "sine", "cos", "cosine", "tan", "tangent"), "Evaluate a trigonometric ratio in degrees."),
)


def get_rules():
    """Return all rules as an immutable tuple."""
    return RULES
