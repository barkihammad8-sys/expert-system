"""A small forward-matching inference engine."""

from dataclasses import dataclass
from typing import List, Optional

from .knowledge_base import Rule, get_rules


@dataclass
class InferenceResult:
    topic: Optional[str]
    matched_rule: Optional[Rule]
    trace: List[str]


class InferenceEngine:
    """Matches input facts (words in a question) against production rules."""

    def __init__(self, rules=None):
        self.rules = tuple(rules or get_rules())

    @staticmethod
    def _normalise(text: str) -> str:
        return " ".join(text.lower().replace("^", "**").split())

    def infer(self, question: str) -> InferenceResult:
        text = self._normalise(question)
        trace = ["Received question and normalised its text."]
        ranked = []
        for rule in self.rules:
            matches = [word for word in rule.keywords if word in text]
            if matches:
                ranked.append((len(matches), rule))
        if not ranked:
            trace.append("No knowledge-base rule matched the question.")
            return InferenceResult(None, None, trace)
        ranked.sort(key=lambda item: item[0], reverse=True)
        rule = ranked[0][1]
        trace.append(f"Matched rule {rule.rule_id}: {rule.description}")
        trace.append(f"Selected topic: {rule.topic}.")
        return InferenceResult(rule.topic, rule, trace)
