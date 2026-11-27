"""Automated tests for the Mathematics Expert System."""

import unittest

from math_expert_system.core import MathematicsExpertSystem
from math_expert_system.inference_engine import InferenceEngine
from math_expert_system.nlp import parse_question
from math_expert_system.solvers import parse_expression


class ParserTests(unittest.TestCase):
    def test_linear_equation_is_parsed(self):
        parsed = parse_question("solve 2*x + 3 = 7")
        self.assertEqual(parsed["operation"], "solve_equation")

    def test_circle_is_parsed(self):
        parsed = parse_question("area of circle radius 4")
        self.assertEqual(parsed["operation"], "circle_area")
        self.assertEqual(parsed["radius"], 4.0)

    def test_expression_parser_rejects_python_code(self):
        with self.assertRaises(ValueError):
            parse_expression("__import__('os').system('echo unsafe')")


class InferenceTests(unittest.TestCase):
    def test_quadratic_rule_wins_over_generic_solve_rule(self):
        result = InferenceEngine().infer("solve x^2 - 5*x + 6 = 0")
        self.assertEqual(result.topic, "algebra")
        self.assertEqual(result.matched_rule.rule_id, "ALG-QUADRATIC")


class ExpertSystemTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.system = MathematicsExpertSystem()

    def test_linear_equation(self):
        result = self.system.ask("solve 2*x + 3 = 7")
        self.assertTrue(result["success"], result)
        self.assertIn("x = 2", result["answer"])

    def test_quadratic_equation(self):
        result = self.system.ask("solve x^2 - 5*x + 6 = 0")
        self.assertTrue(result["success"], result)
        self.assertIn("x = 2", result["answer"])
        self.assertIn("x = 3", result["answer"])

    def test_differentiation(self):
        result = self.system.ask("differentiate x^3 + 2*x")
        self.assertTrue(result["success"], result)
        self.assertEqual(result["answer"], "3*x**2 + 2")

    def test_integration(self):
        result = self.system.ask("integrate 3*x^2")
        self.assertTrue(result["success"], result)
        self.assertEqual(result["answer"], "x**3 + C")

    def test_circle_area(self):
        result = self.system.ask("area of circle radius 4")
        self.assertTrue(result["success"], result)
        self.assertAlmostEqual(float(result["answer"]), 16 * 3.141592653589793)

    def test_rectangle_area(self):
        result = self.system.ask("area of rectangle length 5 width 3")
        self.assertTrue(result["success"], result)
        self.assertAlmostEqual(float(result["answer"]), 15.0)

    def test_triangle_area(self):
        result = self.system.ask("area of triangle base 10 height 6")
        self.assertTrue(result["success"], result)
        self.assertAlmostEqual(float(result["answer"]), 30.0)

    def test_trigonometry(self):
        result = self.system.ask("sin 30")
        self.assertTrue(result["success"], result)
        self.assertAlmostEqual(float(result["answer"]), 0.5)

    def test_invalid_question_returns_helpful_error(self):
        result = self.system.ask("tell me a joke")
        self.assertFalse(result["success"])
        self.assertIn("could not understand", result["error"].lower())


if __name__ == "__main__":
    unittest.main()
