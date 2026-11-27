
from knowledge_base.rules import (
    ALGEBRA_RULES,
    CALCULUS_RULES,
    GEOMETRY_RULES,
    TRIGONOMETRY_RULES,
    RULES
)

from knowledge_base.assertions import ASSERTIONS

print("=" * 55)
print("MATHEMATICS EXPERT SYSTEM - COMPLETE RULE VALIDATION")
print("=" * 55)

# 1. Check domain rule counts
assert len(ALGEBRA_RULES) == 25
assert len(CALCULUS_RULES) == 25
assert len(GEOMETRY_RULES) == 25
assert len(TRIGONOMETRY_RULES) == 25

print("Algebra rules:              ", len(ALGEBRA_RULES))
print("Calculus rules:             ", len(CALCULUS_RULES))
print("Geometry rules:             ", len(GEOMETRY_RULES))
print("Trigonometry rules:          ", len(TRIGONOMETRY_RULES))

# 2. Check total rules
assert len(RULES) == 100
print("----------------------------------------")
print("TOTAL RULES:                 ", len(RULES))

# 3. Check unique rule IDs
rule_ids = [rule["id"] for rule in RULES]

assert len(rule_ids) == len(set(rule_ids))
print("Unique rule IDs:             PASSED")

# 4. Check sequential IDs
expected_ids = (
    [f"ALG_R{i:03d}" for i in range(1, 26)]
    + [f"CAL_R{i:03d}" for i in range(1, 26)]
    + [f"GEO_R{i:03d}" for i in range(1, 26)]
    + [f"TRI_R{i:03d}" for i in range(1, 26)]
)

assert rule_ids == expected_ids
print("Sequential rule IDs:        PASSED")

# 5. Check required fields
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

for rule in RULES:
    for field in required_fields:
        assert field in rule, (
            f"Missing {field} in {rule['id']}"
        )

    assert rule["conditions"]["problem_type"]
    assert rule["conditions"]["required_features"]
    assert rule["assertions"]
    assert rule["action"]
    assert rule["verification"]

print("Required fields:            PASSED")

# 6. Check domain distribution
expected_domains = {
    "Algebra": 25,
    "Calculus": 25,
    "Geometry": 25,
    "Trigonometry": 25
}

for domain, expected_count in expected_domains.items():
    actual_count = sum(
        1 for rule in RULES
        if rule["domain"] == domain
    )

    assert actual_count == expected_count, (
        f"Incorrect rule count for {domain}"
    )

print("Domain distribution:        PASSED")

# 7. Check assertion references
assertion_ids = {
    assertion["id"] for assertion in ASSERTIONS
}

for rule in RULES:
    for assertion_id in rule["assertions"]:
        assert assertion_id in assertion_ids, (
            f"{rule['id']} references missing assertion "
            f"{assertion_id}"
        )

print("Assertion references:       PASSED")

# 8. Check duplicate assertion references inside rules
for rule in RULES:
    assert len(rule["assertions"]) == len(
        set(rule["assertions"])
    ), f"Duplicate assertion in {rule['id']}"

print("Duplicate references:       PASSED")

print("=" * 55)
print("ALL 100 EXPERT RULES VALIDATED SUCCESSFULLY!")
print("=" * 55)
