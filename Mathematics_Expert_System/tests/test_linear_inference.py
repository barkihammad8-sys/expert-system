
from inference_engine.engine import inference_engine

print("=" * 55)
print("LINEAR EQUATION INFERENCE TEST")
print("=" * 55)

facts = [
    "equation",
    "first_degree",
    "one_variable",
    "two_known_sides",
    "variable",
    "x_variable"
]

result = inference_engine.infer(
    facts=facts,
    domain="Algebra",
    problem_type="linear_equation"
)

print("\nInference Status:", result["status"])
print("Rules Fired:", result["rules_fired"])
print("Fired Rule IDs:", result["fired_rule_ids"])
print("Conclusions:", result["conclusions"])

assert result["status"] == "supported"
assert "ALG_R001" in result["fired_rule_ids"]

print("\nLINEAR EQUATION INFERENCE TEST PASSED!")
