
from mathematics_solver.trigonometry import TrigonometrySolver

solver = TrigonometrySolver()

print("=" * 45)
print("TRIGONOMETRY SOLVER TESTING")
print("=" * 45)

# TEST 1: Sine of 30 degrees
result = solver.calculate_ratio("sin", 30)

assert result["status"] == "success"
assert result["result"] == "1/2"

print("Test 1 - Sine 30 degrees:       PASSED")


# TEST 2: Cosine of 60 degrees
result = solver.calculate_ratio("cos", 60)

assert result["result"] == "1/2"

print("Test 2 - Cosine 60 degrees:     PASSED")


# TEST 3: Tangent of 45 degrees
result = solver.calculate_ratio("tan", 45)

assert result["result"] == "1"

print("Test 3 - Tangent 45 degrees:    PASSED")


# TEST 4: Degrees to radians
result = solver.degrees_to_radians(180)

assert result["result"] == "pi"

print("Test 4 - Degrees to radians:    PASSED")


# TEST 5: Radians to degrees
result = solver.radians_to_degrees("pi")

assert result["result"] == "180"

print("Test 5 - Radians to degrees:    PASSED")


# TEST 6: Trigonometric identity
result = solver.simplify_identity(
    "sin(x)**2 + cos(x)**2"
)

assert result["result"] == "1"

print("Test 6 - Identity simplification: PASSED")


# TEST 7: Trigonometric equation
result = solver.solve_equation(
    "sin(x) - 1"
)

assert result["status"] == "success"

print("Test 7 - Equation solving:      PASSED")


# TEST 8: Invalid function
result = solver.calculate_ratio("unknown", 30)

assert result["status"] == "error"

print("Test 8 - Invalid function:      PASSED")


print("-" * 45)
print("ALL TRIGONOMETRY SOLVER TESTS PASSED!")
print("=" * 45)
