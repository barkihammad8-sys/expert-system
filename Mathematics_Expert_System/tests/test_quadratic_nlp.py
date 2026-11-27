
from nlp.processor import nlp_processor

print("=" * 60)
print("QUADRATIC EQUATION NLP TEST")
print("=" * 60)

questions = [
    "Solve the quadratic equation x**2 - 5*x + 6 = 0",
    "Find the roots of x**2 + 3*x + 2 = 0",
    "Solve x**2 - 9 = 0"
]

for question in questions:
    result = nlp_processor.process(question)

    print("\nQuestion:", question)
    print("Status:", result.get("status"))
    print("Domain:", result.get("domain"))
    print("Problem Type:", result.get("problem_type"))
    print("Expression:", result.get("expression"))
    print("Recognized Facts:", result.get("recognized_facts"))
    print("Missing Features:", result.get("missing_features"))
    print("Matched Rule:", result.get("matched_rule"))
    print("-" * 60)
