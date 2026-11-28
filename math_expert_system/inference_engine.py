"""A small rule-matching inference engine."""

from dataclasses import dataclass
from typing import List, Optional

from .knowledge_base import Rule, get_rules


@dataclass
class InferenceResult:
    topic: Optional[str]
    matched_rule: Optional[Rule]
    trace: List[str]


class InferenceEngine:
    """Matches question facts against production rules and records its choice."""

    def __init__(self, rules=None):
        self.rules = tuple(rules or get_rules())

    @staticmethod
    def _normalise(text: str) -> str:
        return " ".join(text.lower().replace("^", "**").split())

    def infer(self, question: str) -> InferenceResult:
        text = self._normalise(question)
        trace = ["Received question and normalised its text."]
        ranked = []
        specificity_weights = {
            "x**3": 30,
            "cubic": 30,
            "x**2": 20,
            "quadratic": 20,
            "linear": 10,
            "circle": 10,
            "rectangle": 10,
            "triangle": 10,
        }
        for rule in self.rules:
            matches = [word for word in rule.keywords if word in text]
            if matches:
                # Degree-specific polynomial rules outrank generic solve rules.
                specificity = sum(specificity_weights.get(word, 1) for word in matches)
                ranked.append((len(matches), specificity, rule))
        if not ranked:
            trace.append("No knowledge-base rule matched the question.")
            return InferenceResult(None, None, trace)
        ranked.sort(key=lambda item: (item[0], item[1]), reverse=True)
        rule = ranked[0][2]
        trace.append(f"Matched rule {rule.rule_id}: {rule.description}")
        trace.append(f"Selected topic: {rule.topic}.")
        return InferenceResult(rule.topic, rule, trace)
