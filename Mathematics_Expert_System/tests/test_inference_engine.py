
from inference_engine.engine import InferenceEngine

engine = InferenceEngine()

print("=" * 45)
print("INFERENCE ENGINE TESTING")
print("=" * 45)

# TEST 1: Supported calculus problem
facts = [
    "function",
    "variable",
    "power_expression"
]

result = engine.infer(
    facts=facts,
    domain="Calculus",
    problem_type="derivative"
)

assert result["status"] == "supported"
assert "CAL_R007" in result["fired_rule_ids"]

print("Test 1 - Power rule:          PASSED")
print("Rules fired:", result["fired_rule_ids"])


# TEST 2: Missing required features
facts = [
    "function",
    "power_expression"
]

result = engine.infer(
    facts=facts,
    domain="Calculus",
    problem_type="derivative"
)

assert result["status"] == "unsupported"
assert result["rules_fired"] == 0

print("Test 2 - Missing features:    PASSED")


# TEST 3: Unsupported problem type
facts = [
    "function",
    "variable",
    "power_expression"
]

result = engine.infer(
    facts=facts,
    domain="Calculus",
    problem_type="advanced_laplace_transform"
)

assert result["status"] == "unsupported"

print("Test 3 - Unsupported type:    PASSED")


# TEST 4: Domain restriction
facts = [
    "function",
    "variable",
    "power_expression"
]

result = engine.infer(
    facts=facts,
    domain="Geometry",
    problem_type="derivative"
)

assert result["status"] == "unsupported"

print("Test 4 - Domain restriction:  PASSED")


# TEST 5: Dictionary input
facts = {
    "function": True,
    "variable": True,
    "power_expression": True
}

result = engine.infer(
    facts=facts,
    domain="Calculus",
    problem_type="derivative"
)

assert result["status"] == "supported"

print("Test 5 - Dictionary input:   PASSED")

print("-" * 45)
print("ALL INFERENCE ENGINE TESTS PASSED!")
print("=" * 45)
