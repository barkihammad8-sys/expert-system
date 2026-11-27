
from knowledge_base.rules import GEOMETRY_RULES
from knowledge_base.assertions import ASSERTIONS

print("=" * 40)
print("GEOMETRY RULE VALIDATION")
print("=" * 40)

# Check total rules
assert len(GEOMETRY_RULES) == 25
print("Geometry rules:             25")

# Check unique IDs
rule_ids = [rule["id"] for rule in GEOMETRY_RULES]
assert len(rule_ids) == len(set(rule_ids))
print("Unique rule IDs:           PASSED")

# Check sequential IDs
expected_ids = [
    f"GEO_R{i:03d}" for i in range(1, 26)
]
assert rule_ids == expected_ids
print("Sequential rule IDs:       PASSED")

# Check required fields
required_fields = [
    "id", "domain", "name", "description",
    "conditions", "assertions", "action", "verification"
]

for rule in GEOMETRY_RULES:
    for field in required_fields:
        assert field in rule, (
            f"Missing {field} in {rule['id']}"
        )

    assert rule["domain"] == "Geometry"
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

for rule in GEOMETRY_RULES:
    for assertion_id in rule["assertions"]:
        assert assertion_id in assertion_ids, (
            f"{rule['id']} references missing assertion "
            f"{assertion_id}"
        )

print("Assertion references:      PASSED")

print("-" * 40)
print("ALL 25 GEOMETRY RULES VALIDATED!")
