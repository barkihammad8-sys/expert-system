
from knowledge_base.rules import TRIGONOMETRY_RULES
from knowledge_base.assertions import ASSERTIONS

print("=" * 40)
print("TRIGONOMETRY RULE VALIDATION")
print("=" * 40)

# Check total rules
assert len(TRIGONOMETRY_RULES) == 25
print("Trigonometry rules:         25")

# Check unique IDs
rule_ids = [rule["id"] for rule in TRIGONOMETRY_RULES]
assert len(rule_ids) == len(set(rule_ids))
print("Unique rule IDs:           PASSED")

# Check sequential IDs
expected_ids = [
    f"TRI_R{i:03d}" for i in range(1, 26)
]
assert rule_ids == expected_ids
print("Sequential rule IDs:       PASSED")

# Check required fields
required_fields = [
    "id", "domain", "name", "description",
    "conditions", "assertions", "action", "verification"
]

for rule in TRIGONOMETRY_RULES:
    for field in required_fields:
        assert field in rule, (
            f"Missing {field} in {rule['id']}"
        )

    assert rule["domain"] == "Trigonometry"
    assert rule["conditions"]["problem_type"]
    assert rule["conditions"]["required_features"]
    assert rule["assertions"]
    assert rule["action"]
    assert rule["verification"]

print("Required fields:           PASSED")

# Check assertion references
assertion_ids = {
    assertion["id"] for assertion in ASSERTIONS
}

for rule in TRIGONOMETRY_RULES:
    for assertion_id in rule["assertions"]:
        assert assertion_id in assertion_ids, (
            f"{rule['id']} references missing assertion "
            f"{assertion_id}"
        )

print("Assertion references:      PASSED")

print("-" * 40)
print("ALL 25 TRIGONOMETRY RULES VALIDATED!")
