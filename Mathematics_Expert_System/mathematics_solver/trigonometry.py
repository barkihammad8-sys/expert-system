
# ============================================================
# MATHEMATICS EXPERT SYSTEM
# TRIGONOMETRY SOLVER
# ============================================================

import sympy as sp


class TrigonometrySolver:

    def __init__(self):
        self.x = sp.symbols("x")

    def calculate_ratio(self, function, angle, unit="degrees"):
        try:
            angle = sp.sympify(angle)

            if unit == "degrees":
                angle = sp.pi * angle / 180
            elif unit != "radians":
                raise ValueError("Invalid angle unit.")

            functions = {
                "sin": sp.sin,
                "cos": sp.cos,
                "tan": sp.tan
            }

            function = function.lower()

            if function not in functions:
                raise ValueError("Unsupported trigonometric function.")

            result = sp.simplify(functions[function](angle))

            if result in [sp.zoo, sp.nan, sp.oo, -sp.oo]:
                raise ValueError("Undefined trigonometric value.")

            return {
                "status": "success",
                "operation": "Trigonometric Ratio",
                "function": function,
                "result": str(result),
                "approximate_result": str(sp.N(result))
            }

        except Exception:
            return {
                "status": "error",
                "message": "Invalid angle or unsupported trigonometric function."
            }

    def degrees_to_radians(self, degrees):
        try:
            angle = sp.sympify(degrees)

            result = sp.simplify(
                angle * sp.pi / 180
            )

            return {
                "status": "success",
                "operation": "Degrees to Radians",
                "result": str(result)
            }

        except Exception:
            return {
                "status": "error",
                "message": "Invalid degree value."
            }

    def radians_to_degrees(self, radians):
        try:
            angle = sp.sympify(radians)

            result = sp.simplify(
                angle * 180 / sp.pi
            )

            return {
                "status": "success",
                "operation": "Radians to Degrees",
                "result": str(result)
            }

        except Exception:
            return {
                "status": "error",
                "message": "Invalid radian value."
            }

    def simplify_identity(self, expression):
        try:
            parsed = sp.sympify(
                expression,
                locals={
                    "sin": sp.sin,
                    "cos": sp.cos,
                    "tan": sp.tan
                }
            )

            result = sp.trigsimp(parsed)

            return {
                "status": "success",
                "operation": "Trigonometric Simplification",
                "result": str(result)
            }

        except Exception:
            return {
                "status": "error",
                "message": "Invalid trigonometric expression."
            }

    def solve_equation(self, expression):
        try:
            equation = sp.sympify(
                expression,
                locals={
                    "sin": sp.sin,
                    "cos": sp.cos,
                    "tan": sp.tan,
                    "x": self.x
                }
            )

            result = sp.solveset(
                equation,
                self.x,
                domain=sp.S.Reals
            )

            if result is sp.S.EmptySet:
                return {
                    "status": "unsupported",
                    "message": "No real solution exists."
                }

            if isinstance(result, sp.ConditionSet):
                return {
                    "status": "unsupported",
                    "message": "The equation could not be solved within the supported scope."
                }

            return {
                "status": "success",
                "operation": "Trigonometric Equation",
                "result": str(result)
            }

        except Exception:
            return {
                "status": "error",
                "message": "Invalid trigonometric equation."
            }


# Create default trigonometry solver
trigonometry_solver = TrigonometrySolver()
