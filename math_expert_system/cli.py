"""Command-line interface for the Mathematics Expert System."""

from .core import MathematicsExpertSystem

EXAMPLES = [
    "solve 2*x + 3 = 7",
    "solve x^2 - 5*x + 6 = 0",
    "differentiate x^3 + 2*x",
    "integrate 3*x^2",
    "area of circle radius 4",
    "circumference of circle radius 4",
    "area of rectangle length 5 width 3",
    "area of triangle base 10 height 6",
    "sin 30",
    "cos 60",
    "simplify x + x + 2",
]


def show_help():
    print("\nSupported examples:")
    for example in EXAMPLES:
        print(f"  • {example}")
    print("Use ^ or ** for powers. Angles are in degrees.\n")


def main():
    system = MathematicsExpertSystem()
    print("=" * 58)
    print("          MATHEMATICS EXPERT SYSTEM")
    print("=" * 58)
    print("Ask a supported math question. Type 'help' or 'quit'.")
    while True:
        try:
            question = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break
        if question.lower() in {"quit", "exit"}:
            print("Goodbye!")
            break
        if question.lower() in {"help", "examples"}:
            show_help()
            continue
        response = system.ask(question)
        if not response["success"]:
            print(f"System: {response['error']}")
            continue
        print(f"\nAnswer: {response['answer']}")
        if response.get("formula"):
            print(f"Formula: {response['formula']}")
        print(f"Explanation: {response['explanation']}")
        status = response["verification"]
        label = "Passed" if status["verified"] is True else "Not independently checked" if status["verified"] is None else "Failed"
        print(f"Verification: {label} — {status['details']}")
        print("Reasoning:")
        for step in response["reasoning_trace"]:
            print(f"  - {step}")


if __name__ == "__main__":
    main()
