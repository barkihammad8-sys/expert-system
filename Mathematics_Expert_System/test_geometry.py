
from knowledge_base.assertions import (
    ASSERTIONS,
    ALGEBRA_ASSERTIONS,
    CALCULUS_ASSERTIONS,
    GEOMETRY_ASSERTIONS,
    TRIGONOMETRY_ASSERTIONS
)

# Check total assertions
assert len(ALGEBRA_ASSERTIONS) == 75
assert len(CALCULUS_ASSERTIONS) == 75
assert len(GEOMETRY_ASSERTIONS) == 75
assert len(TRIGONOMETRY_ASSERTIONS) == 75
assert len(ASSERTIONS) == 300

# Check unique IDs
all_ids = [item["id"] for item in ASSERTIONS]
assert len(all_ids) == len(set(all_ids)), "Duplicate assertion IDs found!"

# Check required fields
required_fields = [
    "id",
    "domain",
    "name",
    "type",
    "description",
    "knowledge",
    "conditions"
]

for assertion in ASSERTIONS:
    for field in required_fields:
        assert field in assertion, (
            f"Missing field {field} in {assertion.get('id')}"
        )

# Check domain counts
expected_domains = {
    "Algebra": 75,
    "Calculus": 75,
    "Geometry": 75,
    "Trigonometry": 75
}

for domain, expected_count in expected_domains.items():
    actual_count = sum(
        1 for item in ASSERTIONS
        if item["domain"] == domain
    )

    assert actual_count == expected_count, (
        f"{domain}: expected {expected_count}, got {actual_count}"
    )

# Check Trigonometry IDs
expected_ids = [
    f"TRI{i:03d}" for i in range(1, 76)
]

actual_ids = [
    item["id"] for item in TRIGONOMETRY_ASSERTIONS
]

assert actual_ids == expected_ids, (
    "Trigonometry assertion IDs are missing or out of order!"
)

# Check Trigonometry domain
for item in TRIGONOMETRY_ASSERTIONS:
    assert item["domain"] == "Trigonometry"

print("========================================")
print("MATHEMATICS ASSERTION VALIDATION")
print("========================================")
print("Algebra assertions:       75")
print("Calculus assertions:      75")
print("Geometry assertions:      75")
print("Trigonometry assertions:  75")
print("----------------------------------------")
print("TOTAL ASSERTIONS:         300")
print("----------------------------------------")
print("Unique IDs:               PASSED")
print("Required fields:          PASSED")
print("Domain validation:        PASSED")
print("Sequential IDs:           PASSED")
print("----------------------------------------")
print("ALL 300 ASSERTIONS VALIDATED SUCCESSFULLY!")
print("========================================")
