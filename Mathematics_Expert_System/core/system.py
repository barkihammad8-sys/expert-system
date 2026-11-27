
# ============================================================
# INTELLIGENT MATHEMATICS EXPERT SYSTEM
# CENTRAL INTEGRATION MODULE
# ============================================================

import ast
from nlp.processor import nlp_processor
from inference_engine.engine import inference_engine

from mathematics_solver.algebra import AlgebraSolver
from mathematics_solver.calculus import CalculusSolver
from mathematics_solver.geometry import GeometrySolver
from mathematics_solver.trigonometry import TrigonometrySolver

from validation.verifier import mathematics_verifier


class MathematicsExpertSystem:

    def __init__(self):

        self.algebra = AlgebraSolver()
        self.calculus = CalculusSolver()
        self.geometry = GeometrySolver()
        self.trigonometry = TrigonometrySolver()

    # --------------------------------------------------------
    # MAIN QUESTION PROCESSOR
    # --------------------------------------------------------

    def process_question(self, user_question):

        if not isinstance(user_question, str) or not user_question.strip():
            return self.error_response(
                "Please enter a mathematical question."
            )

        # STEP 1: Understand the question using NLP

        nlp_result = nlp_processor.process(user_question)

        if nlp_result.get("status") != "recognized":

            return {
                "status": nlp_result.get("status", "unsupported"),
                "message": nlp_result.get(
                    "message",
                    "The system could not understand this question."
                ),
                "nlp_result": nlp_result
            }


        domain = nlp_result.get("domain")
        domain_key = domain.lower() if isinstance(domain, str) else None

        problem_type = nlp_result.get("problem_type")
        expression = nlp_result.get("expression")

        # STEP 2: Run the expert inference engine

        inference_result = inference_engine.infer(
            facts=nlp_result.get("recognized_facts", []),
            domain=domain_key,
            problem_type=problem_type
        )

        if inference_result.get("status") != "supported":

            return {
                "status": "unsupported",
                "message": (
                    "No applicable expert rule was found. "
                    "The system cannot safely solve this problem."
                ),
                "nlp_result": nlp_result,
                "inference_result": inference_result
            }

        # STEP 3: Select the appropriate mathematical solver

    

        solver_result = self.execute_solver(
            domain_key,
            problem_type,
            expression,
            user_question
        )

        if solver_result.get("status") != "success":

            return {
                "status": "failed",
                "message": solver_result.get(
                    "message",
                    "The mathematical solver could not solve this problem."
                ),
                "nlp_result": nlp_result,
                "inference_result": inference_result,
                "solver_result": solver_result
            }

        # STEP 4: Verify the mathematical result


        verification_result = self.verify_result(
            domain_key,
            problem_type,
            expression,
            solver_result
        )

        if verification_result.get("status") != "verified":

            return {
                "status": "verification_failed",
                "message": (
                    "The calculated answer could not be verified. "
                    "The system will not present it as a correct answer."
                ),
                "verification_result": verification_result
            }

        # STEP 5: Return the final answer

        return {
            "status": "success",
            "message": "The problem was solved and verified successfully.",
            "domain": domain,
            "problem_type": problem_type,
            "question": user_question,
            "answer": solver_result.get("answer"),
            "explanation": solver_result.get("explanation", ""),
            "verification": verification_result,
            "rules_fired": inference_result.get("fired_rules", [])
        }

    # --------------------------------------------------------
    # SOLVER DISPATCHER
    # --------------------------------------------------------

    def execute_solver(self, domain, problem_type, expression, question):

        try:

            result = None

            # ALGEBRA

            if domain == "algebra":


                if problem_type == "linear_equation":
                    result = self.algebra.solve_equation(expression)
            
                elif problem_type == "simplify_expression":
                    result = self.algebra.simplify_expression(expression)

                elif problem_type == "factor_expression":
                    result = self.algebra.factor_expression(expression)

                elif problem_type == "expand_expression":
                    result = self.algebra.expand_expression(expression)

            # CALCULUS

            elif domain == "calculus":

                if problem_type == "differentiate":
                    result = self.calculus.differentiate(expression)

                elif problem_type == "integrate":
                    result = self.calculus.integrate(expression)

            # GEOMETRY

            elif domain == "geometry":

                if problem_type == "circle_area":
                    radius = self.extract_number(question, "radius")
                    result = self.geometry.circle_area(radius)

                elif problem_type == "circle_circumference":
                    radius = self.extract_number(question, "radius")
                    result = self.geometry.circle_circumference(radius)

                elif problem_type == "rectangle_area":
                    length = self.extract_number(question, "length")
                    width = self.extract_number(question, "width")
                    result = self.geometry.rectangle_area(length, width)

                elif problem_type == "rectangle_perimeter":
                    length = self.extract_number(question, "length")
                    width = self.extract_number(question, "width")
                    result = self.geometry.rectangle_perimeter(length, width)

                elif problem_type == "triangle_area":
                    base = self.extract_number(question, "base")
                    height = self.extract_number(question, "height")
                    result = self.geometry.triangle_area(base, height)

            # TRIGONOMETRY

            elif domain == "trigonometry":

                if problem_type == "convert_degrees_to_radians":
                    angle = self.extract_angle(question)
                    result = self.trigonometry.degrees_to_radians(angle)

                elif problem_type == "convert_radians_to_degrees":
                    angle = self.extract_angle(question)
                    result = self.trigonometry.radians_to_degrees(angle)

            if result is None:

                return {
                    "status": "unsupported",
                    "message": (
                        "This operation is not yet implemented "
                        "in the mathematical solver."
                    )
                }

            return self.normalize_solver_result(result)

        except Exception:

            return {
                "status": "failed",
                "message": (
                    "The solver encountered an error. "
                    "Please check the mathematical expression and input."
                )
            }

    # --------------------------------------------------------
    # NORMALIZE SOLVER OUTPUT
    # --------------------------------------------------------

    def normalize_solver_result(self, result):

        if isinstance(result, dict):

            if result.get("status") in ("error", "failed", "unsupported"):
                return {
                    "status": "failed",
                    "message": result.get(
                        "message",
                        "The mathematical calculation failed."
                    )
                }

            answer = result.get(
                "answer",
                result.get("result", result.get("solutions"))
            )

            answer = result.get(
                "answer",
                result.get("result", result.get("solutions"))
            )

            # Convert a string representation of a list into a real list.
            if isinstance(answer, str):
                try:
                    parsed_answer = ast.literal_eval(answer)

                    if isinstance(parsed_answer, (list, tuple)):
                        answer = list(parsed_answer)

                except (ValueError, SyntaxError):
                    pass

            if answer is None:
                return {
                    "status": "failed",
                    "message": "The solver did not return an answer."
                }

            return {
                "status": "success",
                "answer": answer,
                "explanation": result.get(
                    "explanation",
                    result.get("message", "")
                )
            }

        if result is None:
            return {
                "status": "failed",
                "message": "The solver returned no result."
            }

        return {
            "status": "success",
            "answer": result,
            "explanation": ""
        }

    # --------------------------------------------------------
    # MATHEMATICAL VERIFICATION DISPATCHER
    # --------------------------------------------------------

    def verify_result(
        self,
        domain,
        problem_type,
        expression,
        solver_result
    ):

        answer = solver_result.get("answer")

        try:

            if domain == "algebra":


                if problem_type == "linear_equation":
                    verification = mathematics_verifier.verify_equation(
                        expression,
                        answer
                    )

                else:
                    verification = mathematics_verifier.verify_equivalence(
                        expression,
                        answer
                    )

            elif domain == "calculus":

                if problem_type == "differentiate":
                    verification = mathematics_verifier.verify_derivative(
                        expression,
                        answer
                    )

                elif problem_type == "integrate":
                    verification = mathematics_verifier.verify_integral(
                        expression,
                        str(answer).replace("+ C", "").strip()
                    )

                else:
                    return {
                        "status": "unsupported",
                        "message": "No verification method is available."
                    }

            else:

                return {
                    "status": "unsupported",
                    "message": (
                        "Independent verification for this operation "
                        "has not yet been implemented."
                    )
                }

            return verification

        except Exception:

            return {
                "status": "error",
                "message": "Mathematical verification encountered an error."
            }

    # --------------------------------------------------------
    # INPUT EXTRACTION HELPERS
    # --------------------------------------------------------

    def extract_number(self, question, keyword):

        import re

        pattern = rf"{keyword}\s*(?:of|is|=|:)?\s*(-?\d+(?:\.\d+)?)"

        match = re.search(pattern, question, re.IGNORECASE)

        if not match:
            raise ValueError(f"Missing {keyword}.")

        return float(match.group(1))

    def extract_angle(self, question):

        import re

        match = re.search(
            r"(-?\d+(?:\.\d+)?)\s*(?:degrees?|°|radians?)",
            question,
            re.IGNORECASE
        )

        if not match:
            raise ValueError("Missing angle.")

        return float(match.group(1))

    # --------------------------------------------------------
    # ERROR RESPONSE
    # --------------------------------------------------------

    def error_response(self, message):

        return {
            "status": "error",
            "message": message
        }


# Create the main expert system

mathematics_expert_system = MathematicsExpertSystem()
