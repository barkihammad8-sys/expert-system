
from core.system import mathematics_expert_system

print("=" * 60)
print("LINEAR EQUATION END-TO-END TEST")
print("=" * 60)

question = "Solve the equation 2*x + 5 = 15"

result = mathematics_expert_system.process_question(question)

print("\nQuestion:", question)
print("Status:", result.get("status"))
print("Message:", result.get("message"))
print("Domain:", result.get("domain"))
print("Problem Type:", result.get("problem_type"))
print("Answer:", result.get("answer"))

print("\nVerification:")
print(result.get("verification"))

print("\nRules Fired:")
for rule in result.get("rules_fired", []):
    print(rule.get("id"), "-", rule.get("name"))

# Validation
assert result["status"] == "success"
assert result["domain"] == "Algebra"
assert result["problem_type"] == "linear_equation"
assert result["answer"] == [5]
assert result["verification"]["status"] == "verified"

assert any(
    rule["id"] == "ALG_R001"
    for rule in result["rules_fired"]
)

print("\nALL END-TO-END TESTS PASSED!")
