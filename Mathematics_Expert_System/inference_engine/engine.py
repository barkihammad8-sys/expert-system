
# ============================================================
# MATHEMATICS EXPERT SYSTEM
# FORWARD-CHAINING INFERENCE ENGINE
# ============================================================

from knowledge_base.rules import RULES


class InferenceEngine:

    def __init__(self, rules=None):
        """
        Initialize the inference engine.

        If no custom rules are supplied, use all
        100 mathematics expert rules.
        """
        self.rules = rules if rules is not None else RULES

    @staticmethod
    def normalize_facts(facts):
        """
        Convert recognized facts into a set of
        lowercase feature names.
        """

        if facts is None:
            return set()

        if isinstance(facts, str):
            facts = [facts]

        if isinstance(facts, dict):
            return {
                str(key).strip().lower()
                for key, value in facts.items()
                if value
            }

        return {
            str(fact).strip().lower()
            for fact in facts
            if str(fact).strip()
        }

    def infer(self, facts, domain=None, problem_type=None):
        """
        Perform forward-chaining inference.

        Parameters:
            facts: recognized problem features
            domain: Algebra, Calculus, Geometry,
                    or Trigonometry
            problem_type: requested mathematical
                          problem type

        Returns:
            Dictionary containing inference results.
        """

        # Step 1: Initialize working memory
        working_memory = self.normalize_facts(facts)

        initial_facts = set(working_memory)

        normalized_domain = (
            domain.strip().lower()
            if isinstance(domain, str) and domain.strip()
            else None
        )

        normalized_problem = (
            problem_type.strip().lower()
            if isinstance(problem_type, str)
            and problem_type.strip()
            else None
        )

        fired_rules = []
        fired_rule_ids = set()

        # Step 2: Forward-chaining cycle
        changed = True

        while changed:

            changed = False

            for rule in self.rules:

                rule_id = rule["id"]

                # Avoid firing the same rule twice
                if rule_id in fired_rule_ids:
                    continue

                # Check mathematical domain
                rule_domain = rule["domain"].lower()

                if (
                    normalized_domain is not None
                    and rule_domain != normalized_domain
                ):
                    continue

                conditions = rule["conditions"]

                # Check problem type
                rule_problem = (
                    conditions["problem_type"].lower()
                )

                if (
                    normalized_problem is not None
                    and rule_problem != normalized_problem
                ):
                    continue

                # Check required features
                required_features = {
                    str(feature).strip().lower()
                    for feature in
                    conditions["required_features"]
                }

                # A rule fires only if all its
                # required features are available.
                if required_features.issubset(
                    working_memory
                ):

                    fired_rules.append(rule)

                    fired_rule_ids.add(rule_id)

                    # Add derived knowledge to
                    # working memory.
                    working_memory.add(
                        f"rule_fired:{rule_id}".lower()
                    )

                    working_memory.add(
                        f"supported_method:{rule_problem}".lower()
                    )

                    changed = True

        # Step 3: Find the closest applicable rules
        # for explaining missing features.
        candidate_rules = []

        for rule in self.rules:

            if normalized_domain is not None:
                if rule["domain"].lower() != normalized_domain:
                    continue

            if normalized_problem is not None:
                if (
                    rule["conditions"]["problem_type"].lower()
                    != normalized_problem
                ):
                    continue

            required = {
                str(feature).strip().lower()
                for feature in
                rule["conditions"]["required_features"]
            }

            missing = sorted(required - initial_facts)

            matched = sorted(required & initial_facts)

            candidate_rules.append({
                "rule_id": rule["id"],
                "rule_name": rule["name"],
                "matched_features": matched,
                "missing_features": missing,
                "matched_count": len(matched),
                "required_count": len(required)
            })

        # Rank candidates by number of matched features
        candidate_rules.sort(
            key=lambda item: (
                item["matched_count"],
                -len(item["missing_features"])
            ),
            reverse=True
        )

        # Step 4: Prepare conclusions
        conclusions = []

        for rule in fired_rules:
            conclusions.append({
                "rule_id": rule["id"],
                "method": rule["name"],
                "action": rule["action"],
                "verification": rule["verification"]
            })

        # Step 5: Return inference results
        if fired_rules:
            status = "supported"
            message = (
                "Applicable mathematical expert rules "
                "were successfully identified."
            )
        else:
            status = "unsupported"
            message = (
                "No expert rule matched the recognized "
                "facts. The system cannot safely select "
                "a mathematical method."
            )

        best_candidate = (
            candidate_rules[0]
            if candidate_rules
            else None
        )

        return {
            "status": status,
            "message": message,
            "domain": domain,
            "problem_type": problem_type,
            "recognized_facts": sorted(initial_facts),
            "working_memory": sorted(working_memory),
            "rules_fired": len(fired_rules),
            "fired_rule_ids": [
                rule["id"] for rule in fired_rules
            ],
            "fired_rules": [
                {
                    "id": rule["id"],
                    "name": rule["name"],
                    "action": rule["action"],
                    "verification": rule["verification"]
                }
                for rule in fired_rules
            ],
            "conclusions": conclusions,
            "best_candidate": best_candidate,
            "candidate_rules": candidate_rules[:5]
        }


# Create the default inference engine
inference_engine = InferenceEngine()
