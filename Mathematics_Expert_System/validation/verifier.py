
# ============================================================
# MATHEMATICS EXPERT SYSTEM
# MATHEMATICAL VERIFICATION ENGINE
# ============================================================

import sympy as sp


class MathematicsVerifier:

    def __init__(self):
        self.x, self.y, self.z = sp.symbols("x y z")

        self.symbols = {
            "x": self.x,
            "y": self.y,
            "z": self.z
        }

    def parse_expression(self, expression):
        return sp.sympify(
            expression,
            locals=self.symbols
        )

    # --------------------------------------------------------
    # 1. Verify algebraic equation solutions
    # --------------------------------------------------------

    
    def verify_equation(self, equation, solutions):

        try:
            equation = str(equation).strip()

            # Define supported variables
            variables = {
                "x": self.x,
                "y": self.y,
                "z": self.z
            }

            # Parse both sides of the equation
            if "=" in equation:

                if equation.count("=") != 1:
                    raise ValueError("Invalid equation format.")

                left_side, right_side = equation.split("=")

                lhs = sp.sympify(left_side, locals=variables)
                rhs = sp.sympify(right_side, locals=variables)

                original = lhs - rhs

            else:
                original = self.parse_expression(equation)

            if not isinstance(solutions, (list, tuple, set)):
                solutions = [solutions]

            verified = []

            for solution in solutions:

                value = self.parse_expression(solution)

                substituted = sp.simplify(
                    original.subs(self.x, value)
                )

                verified.append({
                    "solution": str(value),
                    "valid": substituted == 0
                })

            all_valid = (
                len(verified) > 0
                and all(item["valid"] for item in verified)
            )

            return {
                "status": "verified" if all_valid else "failed",
                "operation": "Equation Verification",
                "verified_solutions": verified,
                "message": (
                    "All supplied solutions satisfy the equation."
                    if all_valid
                    else "One or more supplied solutions are incorrect."
                )
            }

        except Exception:
            return {
                "status": "error",
                "message": "Unable to verify the equation."
            }


    # --------------------------------------------------------
    # 2. Verify a derivative
    # --------------------------------------------------------

    def verify_derivative(self, original, claimed):

        try:
            function = self.parse_expression(original)
            claimed_derivative = self.parse_expression(claimed)

            actual_derivative = sp.diff(
                function,
                self.x
            )

            difference = sp.simplify(
                actual_derivative - claimed_derivative
            )

            valid = difference == 0

            return {
                "status": "verified" if valid else "failed",
                "operation": "Derivative Verification",
                "expected": str(actual_derivative),
                "claimed": str(claimed_derivative),
                "message": (
                    "The derivative is mathematically correct."
                    if valid
                    else "The claimed derivative is incorrect."
                )
            }

        except Exception:
            return {
                "status": "error",
                "message": "Unable to verify the derivative."
            }

    # --------------------------------------------------------
    # 3. Verify an indefinite integral
    # --------------------------------------------------------

    def verify_integral(self, original, claimed):

        try:
            function = self.parse_expression(original)
            antiderivative = self.parse_expression(claimed)

            calculated_derivative = sp.diff(
                antiderivative,
                self.x
            )

            difference = sp.simplify(
                calculated_derivative - function
            )

            valid = difference == 0

            return {
                "status": "verified" if valid else "failed",
                "operation": "Integration Verification",
                "expected_derivative": str(function),
                "actual_derivative": str(calculated_derivative),
                "message": (
                    "The antiderivative is mathematically correct."
                    if valid
                    else "The claimed antiderivative is incorrect."
                )
            }

        except Exception:
            return {
                "status": "error",
                "message": "Unable to verify the integral."
            }

    # --------------------------------------------------------
    # 4. Verify mathematical equivalence
    # --------------------------------------------------------

    def verify_equivalence(self, expected, claimed):

        try:
            first = self.parse_expression(expected)
            second = self.parse_expression(claimed)

            difference = sp.simplify(first - second)

            valid = difference == 0

            return {
                "status": "verified" if valid else "failed",
                "operation": "Mathematical Equivalence",
                "expected": str(first),
                "claimed": str(second),
                "message": (
                    "Both expressions are mathematically equivalent."
                    if valid
                    else "The expressions are not equivalent."
                )
            }

        except Exception:
            return {
                "status": "error",
                "message": "Unable to compare the expressions."
            }


# Create default verification engine
mathematics_verifier = MathematicsVerifier()
