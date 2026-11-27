
# ============================================================
# END-TO-END TESTING
# INTELLIGENT MATHEMATICS EXPERT SYSTEM
# ============================================================

from core.system import mathematics_expert_system


def run_test(test_name, question, expected_domain=None):

    print(f"\n{test_name}")
    print("-" * 50)

    result = mathematics_expert_system.process_question(question)

    print("Question:", question)
    print("Status:", result.get("status"))
    print("Message:", result.get("message"))

    if result.get("status") == "success":

        print("Domain:", result.get("domain"))
        print("Problem:", result.get("problem_type"))
        print("Answer:", result.get("answer"))

    if expected_domain:

        assert result.get("domain") == expected_domain, (
            f"Expected domain {expected_domain}, "
            f"received {result.get('domain')}"
        )

    return result


print("=" * 60)
print("END-TO-END MATHEMATICS EXPERT SYSTEM TEST")
print("=" * 60)


# TEST 1: Algebra

algebra_result = run_test(
    "TEST 1 - ALGEBRA",
    "Solve the equation 2*x + 5 = 15",
    "algebra"
)


# TEST 2: Calculus

calculus_result = run_test(
    "TEST 2 - CALCULUS",
    "Find the derivative of x**3",
    "calculus"
)


# TEST 3: Geometry

geometry_result = run_test(
    "TEST 3 - GEOMETRY",
    "Find the area of a circle with radius 5",
    "geometry"
)


# TEST 4: Trigonometry

trig_result = run_test(
    "TEST 4 - TRIGONOMETRY",
    "Convert 180 degrees to radians",
    "trigonometry"
)


# TEST 5: Unsupported question

unsupported_result = run_test(
    "TEST 5 - UNSUPPORTED QUESTION",
    "Explain quantum mechanics"
)

assert unsupported_result["status"] in (
    "unsupported",
    "incomplete"
)


print("\n" + "=" * 60)
print("END-TO-END TESTING FINISHED")
print("=" * 60)
