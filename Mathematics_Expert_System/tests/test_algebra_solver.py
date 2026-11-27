
from mathematics_solver.algebra import AlgebraSolver

solver = AlgebraSolver()

print("=" * 45)
print("ALGEBRA SOLVER TESTING")
print("=" * 45)

# TEST 1: Linear equation
result = solver.solve_equation("2*x + 5 - 15")

assert result["status"] == "success"
assert "5" in result["result"]

print("Test 1 - Linear equation:       PASSED")
print("Result:", result["result"])


# TEST 2: Quadratic equation
result = solver.solve_equation("x**2 - 5*x + 6")

assert result["status"] == "success"

print("Test 2 - Quadratic equation:    PASSED")
print("Result:", result["result"])


# TEST 3: Simplification
result = solver.simplify_expression("2*x + 3*x")

assert result["result"] == "5*x"

print("Test 3 - Simplification:        PASSED")


# TEST 4: Factorization
result = solver.factor_expression("x**2 - 5*x + 6")

assert result["status"] == "success"

print("Test 4 - Factorization:         PASSED")
print("Result:", result["result"])


# TEST 5: Expansion
result = solver.expand_expression("(x + 2)**2")

assert result["result"] == "x**2 + 4*x + 4"

print("Test 5 - Expansion:             PASSED")


# TEST 6: Invalid expression
result = solver.solve_equation("x + = 5")

assert result["status"] == "error"

print("Test 6 - Invalid expression:    PASSED")

print("-" * 45)
print("ALL ALGEBRA SOLVER TESTS PASSED!")
print("=" * 45)
