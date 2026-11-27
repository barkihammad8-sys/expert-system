
# ============================================================
# MATHEMATICS EXPERT SYSTEM
# CALCULUS SOLVER
# ============================================================

import sympy as sp


class CalculusSolver:

    def __init__(self):
        self.x = sp.symbols("x")

    def differentiate(self, expression, order=1):
        try:
            parsed = sp.sympify(expression)

            if not isinstance(order, int) or order < 1 or order > 10:
                raise ValueError("Invalid derivative order.")

            result = sp.diff(parsed, self.x, order)

            return {
                "status": "success",
                "operation": "Differentiation",
                "input": str(expression),
                "order": order,
                "result": str(result)
            }

        except Exception:
            return {
                "status": "error",
                "message": "Invalid expression or derivative order."
            }

    def integrate(self, expression):
        try:
            parsed = sp.sympify(expression)

            result = sp.integrate(parsed, self.x)

            return {
                "status": "success",
                "operation": "Integration",
                "input": str(expression),
                "result": str(result) + " + C"
            }

        except Exception:
            return {
                "status": "error",
                "message": "Invalid integration expression."
            }

    def definite_integral(self, expression, lower, upper):
        try:
            parsed = sp.sympify(expression)

            lower = sp.sympify(lower)
            upper = sp.sympify(upper)

            result = sp.integrate(
                parsed,
                (self.x, lower, upper)
            )

            return {
                "status": "success",
                "operation": "Definite Integration",
                "input": str(expression),
                "lower_limit": str(lower),
                "upper_limit": str(upper),
                "result": str(result)
            }

        except Exception:
            return {
                "status": "error",
                "message": "Invalid definite integration problem."
            }

    def calculate_limit(self, expression, point, direction="+-"):
        try:
            parsed = sp.sympify(expression)
            point = sp.sympify(point)

            if direction not in ["+", "-", "+-"]:
                raise ValueError("Invalid limit direction.")

            result = sp.limit(
                parsed,
                self.x,
                point,
                dir=direction
            )

            return {
                "status": "success",
                "operation": "Limit",
                "input": str(expression),
                "point": str(point),
                "result": str(result)
            }

        except Exception:
            return {
                "status": "error",
                "message": "Invalid limit expression."
            }


# Create default calculus solver
calculus_solver = CalculusSolver()
