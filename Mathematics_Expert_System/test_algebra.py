
from knowledge_base.rules import ALGEBRA_RULES, RULES
from knowledge_base.assertions import ASSERTIONS

# Check rule count
assert len(ALGEBRA_RULES) == 25
assert len(RULES) == 25

# Check unique rule IDs
rule_ids = [rule["id"] for rule in ALGEBRA_RULES]
assert len(rule_ids) == len(set(rule_ids))

# Check sequential IDs
expected_ids = [
    f"ALG_R{i:03d}" for i in range(1, 26)
]

assert rule_ids == expected_ids

# Check required fields
required_fields = [
    "id",
    "domain",
    "name",
    "description",
    "conditions",
    "assertions",
    "action",
    "verification"
]

for rule in ALGEBRA_RULES:
    for field in required_fields:
        assert field in rule, (
            f"Missing {field} in {rule.get('id')}"
        )

    assert rule["domain"] == "Algebra"

    assert rule["conditions"]["problem_type"]
    assert rule["conditions"]["required_features"]
    assert rule["action"]
    assert rule["verification"]

# Check that every referenced assertion exists
assertion_ids = {
    assertion["id"] for assertion in ASSERTIONS
}

for rule in ALGEBRA_RULES:
    for assertion_id in rule["assertions"]:
        assert assertion_id in assertion_ids, (
            f"{rule['id']} references missing assertion "
            f"{assertion_id}"
        )

print("========================================")
print("ALGEBRA RULE VALIDATION")
print("========================================")
print("Algebra rules:             25")
print("Unique rule IDs:           PASSED")
print("Sequential rule IDs:       PASSED")
print("Required fields:           PASSED")
print("Domain validation:         PASSED")
print("Assertion references:      PASSED")
print("----------------------------------------")
print("ALL 25 ALGEBRA RULES VALIDATED!")
print("========================================")
