
from nlp.processor import nlp_processor

print("=" * 50)
print("ALGEBRA NLP RECOGNITION TEST")
print("=" * 50)

question = "Solve the equation 2*x + 5 = 15"

result = nlp_processor.process(question)

print("Question:", question)
print("Status:", result["status"])
print("Domain:", result["domain"])
print("Problem Type:", result["problem_type"])
print("Expression:", result["expression"])
print("Recognized Facts:", result["recognized_facts"])
print("Missing Features:", result["missing_features"])

assert result["domain"] == "Algebra"
assert result["problem_type"] == "linear_equation"
assert result["status"] == "recognized"

print("\nALGEBRA NLP TEST PASSED!")
print("\nCOMPLETE NLP RESULT:")
print(result)