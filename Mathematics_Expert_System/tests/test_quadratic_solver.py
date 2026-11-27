
from mathematics_solver.algebra import AlgebraSolver

print("=" * 60)
print("QUADRATIC EQUATION SOLVER TEST")
print("=" * 60)

solver = AlgebraSolver()

equations = [
    "x**2 - 5*x + 6 = 0",
    "x**2 + 3*x + 2 = 0",
    "x**2 - 9 = 0"
]

for equation in equations:

    print("\nEquation:", equation)

    result = solver.solve_equation(equation)

    print("Solver Output:", result)

    print("-" * 60)
