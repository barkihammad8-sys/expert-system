
from knowledge_base.rules import RULES

print("=" * 65)
print("MATHEMATICS EXPERT RULE FEATURE INSPECTION")
print("=" * 65)

for rule in RULES:

    print("\nRule ID:", rule["id"])
    print("Domain:", rule["domain"])
    print("Problem Type:", rule["conditions"]["problem_type"])

    print("Required Features:")

    for feature in rule["conditions"]["required_features"]:
        print("  -", feature)

    print("-" * 65)

print("\nTotal Rules Inspected:", len(RULES))
