
from validation.verifier import MathematicsVerifier

verifier = MathematicsVerifier()

print("=" * 50)
print("MATHEMATICAL VERIFICATION TESTING")
print("=" * 50)


# TEST 1: Correct linear equation solution
result = verifier.verify_equation(
    "2*x + 5 - 15",
    [5]
)

assert result["status"] == "verified"

print("Test 1 - Correct equation:          PASSED")


# TEST 2: Incorrect equation solution
result = verifier.verify_equation(
    "2*x + 5 - 15",
    [4]
)

assert result["status"] == "failed"

print("Test 2 - Incorrect equation:        PASSED")


# TEST 3: Correct derivative
result = verifier.verify_derivative(
    "x**3",
    "3*x**2"
)

assert result["status"] == "verified"

print("Test 3 - Correct derivative:        PASSED")


# TEST 4: Incorrect derivative
result = verifier.verify_derivative(
    "x**3",
    "3*x"
)

assert result["status"] == "failed"

print("Test 4 - Incorrect derivative:      PASSED")


# TEST 5: Correct integration
result = verifier.verify_integral(
    "3*x**2",
    "x**3"
)

assert result["status"] == "verified"

print("Test 5 - Correct integration:       PASSED")


# TEST 6: Incorrect integration
result = verifier.verify_integral(
    "3*x**2",
    "x**2"
)

assert result["status"] == "failed"

print("Test 6 - Incorrect integration:     PASSED")


# TEST 7: Equivalent expressions
result = verifier.verify_equivalence(
    "x**2 + 2*x + 1",
    "(x + 1)**2"
)

assert result["status"] == "verified"

print("Test 7 - Equivalent expressions:    PASSED")


# TEST 8: Non-equivalent expressions
result = verifier.verify_equivalence(
    "x**2 + 2",
    "x**2 + 5"
)

assert result["status"] == "failed"

print("Test 8 - Non-equivalent expressions: PASSED")


print("-" * 50)
print("ALL VERIFICATION TESTS PASSED!")
print("=" * 50)
