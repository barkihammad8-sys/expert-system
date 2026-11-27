
from validation.verifier import mathematics_verifier

print("=" * 55)
print("LINEAR EQUATION VERIFICATION TEST")
print("=" * 55)

equation = "2*x + 5 = 15"

# Test 1: Correct solution
correct_result = mathematics_verifier.verify_equation(
    equation, [5]
)

print("\nTEST 1 - Correct Solution")
print(correct_result)

assert correct_result["status"] == "verified"
assert correct_result["verified_solutions"][0]["valid"] is True

# Test 2: Incorrect solution
incorrect_result = mathematics_verifier.verify_equation(
    equation, [10]
)

print("\nTEST 2 - Incorrect Solution")
print(incorrect_result)

assert incorrect_result["status"] == "failed"
assert incorrect_result["verified_solutions"][0]["valid"] is False

print("\nALL LINEAR VERIFICATION TESTS PASSED!")
