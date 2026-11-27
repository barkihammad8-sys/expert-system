
from mathematics_solver.calculus import CalculusSolver

solver = CalculusSolver()

print("=" * 45)
print("CALCULUS SOLVER TESTING")
print("=" * 45)

# TEST 1: First derivative
result = solver.differentiate("x**3")

assert result["status"] == "success"
assert result["result"] == "3*x**2"

print("Test 1 - First derivative:       PASSED")
print("Result:", result["result"])


# TEST 2: Second derivative
result = solver.differentiate("x**4", order=2)

assert result["status"] == "success"
assert result["result"] == "12*x**2"

print("Test 2 - Second derivative:      PASSED")


# TEST 3: Indefinite integration
result = solver.integrate("3*x**2")

assert result["status"] == "success"
assert result["result"] == "x**3 + C"

print("Test 3 - Integration:            PASSED")


# TEST 4: Definite integration
result = solver.definite_integral("x**2", 0, 2)

assert result["status"] == "success"
assert result["result"] == "8/3"

print("Test 4 - Definite integration:   PASSED")


# TEST 5: Limit
result = solver.calculate_limit("x**2 + 3*x", 2)

assert result["status"] == "success"
assert result["result"] == "10"

print("Test 5 - Limit:                  PASSED")


# TEST 6: Invalid derivative order
result = solver.differentiate("x**3", order=0)

assert result["status"] == "error"

print("Test 6 - Invalid derivative:     PASSED")

print("-" * 45)
print("ALL CALCULUS SOLVER TESTS PASSED!")
print("=" * 45)
