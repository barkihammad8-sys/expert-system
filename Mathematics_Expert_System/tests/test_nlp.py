
from nlp.processor import MathematicsNLP

processor = MathematicsNLP()

print("=" * 50)
print("NLP PROCESSOR TESTING")
print("=" * 50)


# TEST 1: Calculus derivative
result = processor.process(
    "Find the derivative of x**2"
)

assert result["domain"] == "Calculus"
assert result["problem_type"] == "derivative"
assert result["status"] == "recognized"

print("Test 1 - Calculus derivative:       PASSED")


# TEST 2: Geometry circle area
result = processor.process(
    "Find the area of a circle with radius 7"
)

assert result["domain"] == "Geometry"
assert result["problem_type"] == "circle_area"
assert result["status"] == "recognized"

print("Test 2 - Geometry circle area:      PASSED")


# TEST 3: Trigonometry sine
result = processor.process(
    "Find sine of 30 degrees"
)

assert result["domain"] == "Trigonometry"
assert result["problem_type"] == "sine_ratio"

print("Test 3 - Trigonometry sine:         PASSED")


# TEST 4: Algebra quadratic
result = processor.process(
    "Solve the quadratic equation x**2 - 5*x + 6 = 0"
)

assert result["domain"] == "Algebra"
assert result["problem_type"] == "quadratic_equation"

print("Test 4 - Algebra quadratic:         PASSED")


# TEST 5: Incomplete problem
result = processor.process(
    "Find the area"
)

assert result["status"] == "unsupported" or result["status"] == "incomplete"

print("Test 5 - Incomplete problem:        PASSED")


# TEST 6: Empty input
result = processor.process("")

assert result["status"] == "invalid"

print("Test 6 - Empty input:               PASSED")


# TEST 7: Unsupported topic
result = processor.process(
    "Explain quantum mechanics"
)

assert result["status"] == "unsupported"

print("Test 7 - Unsupported topic:         PASSED")


print("-" * 50)
print("ALL NLP TESTS PASSED!")
print("=" * 50)
