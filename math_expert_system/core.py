"""Application coordinator for the Mathematics Expert System."""

from typing import Any, Dict

from .inference_engine import InferenceEngine
from .nlp import parse_question
from .solvers import (
    differentiate, integrate, simplify, solve_equation, solve_geometry, solve_trig,
)
from .verifier import verify_result


class MathematicsExpertSystem:
    """Coordinates the complete question-to-answer reasoning pipeline."""

    def __init__(self):
        self.inference_engine = InferenceEngine()

    def ask(self, question: str) -> Dict[str, Any]:
        inference = self.inference_engine.infer(question)
        try:
            parameters = parse_question(question)
            operation = parameters["operation"]
            if operation == "solve_equation":
                result = solve_equation(parameters["left"], parameters["right"])
            elif operation == "differentiate":
                result = differentiate(parameters["expression"], parameters["variable"])
            elif operation == "integrate":
                result = integrate(parameters["expression"], parameters["variable"])
            elif operation == "simplify":
                result = simplify(parameters["expression"])
            elif operation in ("circle_area", "circumference", "rectangle_area", "rectangle_perimeter", "triangle_area"):
                result = solve_geometry(operation, parameters)
            elif operation == "trig":
                result = solve_trig(parameters["function"], parameters["angle"])
            else:
                raise ValueError(f"Unsupported operation: {operation}")

            verification = verify_result(operation, result, parameters)
            trace = list(inference.trace)
            if inference.matched_rule is None:
                trace.append("The parser recognised a supported operation, but no named rule matched.")
            trace.append(f"Executed operation: {operation}.")
            trace.append(verification["details"])
            return {
                "success": True,
                "question": question,
                "topic": inference.topic or operation,
                "operation": operation,
                "answer": result["answer"],
                "latex_answer": result.get("latex_answer"),
                "numeric_answer": result.get("numeric_answer"),
                "explanation": result.get("explanation", ""),
                "formula": result.get("formula"),
                "verification": verification,
                "reasoning_trace": trace,
            }
        except (ValueError, RuntimeError, TypeError, KeyError, ZeroDivisionError) as exc:
            return {
                "success": False,
                "question": question,
                "error": str(exc),
                "reasoning_trace": inference.trace,
            }
