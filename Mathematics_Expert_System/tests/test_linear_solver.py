
from mathematics_solver.algebra import AlgebraSolver

solver = AlgebraSolver()

print("=" * 55)
print("LINEAR EQUATION SOLVER TEST")
print("=" * 55)

equation = "2*x + 5 = 15"

result = solver.solve_equation(equation)

print("\nInput Equation:", equation)
print("Solver Status:", result["status"])
print("Solver Result:", result.get("result"))
print("Message:", result.get("message", "None"))

assert result["status"] == "success"
assert result["result"] == "[5]"

print("\nLINEAR EQUATION SOLVER TEST PASSED!")
