
# ============================================================
# MATHEMATICS EXPERT SYSTEM
# ALGEBRA SOLVER
# ============================================================

import sympy as sp


class AlgebraSolver:

    def __init__(self):
        self.x, self.y, self.z = sp.symbols("x y z")


    def solve_equation(self, expression):
        try:
            # Define supported mathematical variables
            variables = {
                "x": self.x,
                "y": self.y,
                "z": self.z
            }

            expression = str(expression).strip()

            # Separate left-hand side and right-hand side
            if "=" in expression:

                if expression.count("=") != 1:
                    return {
                        "status": "error",
                        "message": "Invalid equation format."
                    }

                left_side, right_side = expression.split("=")

                lhs = sp.sympify(left_side, locals=variables)
                rhs = sp.sympify(right_side, locals=variables)

                equation = sp.Eq(lhs, rhs)

            else:
                # Treat an expression as equal to zero
                equation = sp.Eq(
                    sp.sympify(expression, locals=variables),
                    0
                )

            # Solve the equation
            result = sp.solve(equation)

            if not result:
                return {
                    "status": "unsupported",
                    "message": "No solution could be determined."
                }

            return {
                "status": "success",
                "operation": "Solve Equation",
                "input": expression,
                "result": str(result)
            }

        except Exception:
            return {
                "status": "error",
                "message": "Invalid algebraic equation."
            }

    

    def simplify_expression(self, expression):
        try:
            parsed = sp.sympify(expression)

            result = sp.simplify(parsed)

            return {
                "status": "success",
                "operation": "Simplification",
                "input": str(expression),
                "result": str(result)
            }

        except Exception:
            return {
                "status": "error",
                "message": "Invalid algebraic expression."
            }

    def factor_expression(self, expression):
        try:
            parsed = sp.sympify(expression)

            result = sp.factor(parsed)

            return {
                "status": "success",
                "operation": "Factorization",
                "input": str(expression),
                "result": str(result)
            }

        except Exception:
            return {
                "status": "error",
                "message": "Invalid algebraic expression."
            }

    def expand_expression(self, expression):
        try:
            parsed = sp.sympify(expression)

            result = sp.expand(parsed)

            return {
                "status": "success",
                "operation": "Expansion",
                "input": str(expression),
                "result": str(result)
            }

        except Exception:
            return {
                "status": "error",
                "message": "Invalid algebraic expression."
            }


# Create default algebra solver
algebra_solver = AlgebraSolver()
