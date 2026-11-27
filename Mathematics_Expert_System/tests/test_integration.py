
from core.system import mathematics_expert_system

print("=" * 55)
print("MATHEMATICS EXPERT SYSTEM - INTEGRATION TEST")
print("=" * 55)

# TEST 1: Empty input

result = mathematics_expert_system.process_question("")

assert result["status"] == "error"

print("Test 1 - Empty input:                 PASSED")


# TEST 2: Unsupported question

result = mathematics_expert_system.process_question(
    "Explain quantum mechanics"
)

assert result["status"] in ("unsupported", "incomplete")

print("Test 2 - Unsupported question:        PASSED")


# TEST 3: System returns a structured response

result = mathematics_expert_system.process_question(
    "Find the derivative of x**3"
)

assert isinstance(result, dict)
assert "status" in result

print("Test 3 - Structured response:         PASSED")


print("-" * 55)
print("INITIAL INTEGRATION TESTS COMPLETED")
print("=" * 55)
