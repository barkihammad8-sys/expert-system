
# ============================================================
# MATHEMATICS EXPERT SYSTEM
# NATURAL LANGUAGE PROCESSOR
# ============================================================

import re

from knowledge_base.rules import RULES


class MathematicsNLP:

    def __init__(self):

        self.rules = RULES

        self.domain_keywords = {

            "Algebra": [
                "algebra", "equation", "polynomial",
                "factor", "simplify", "expand",
                "inequality", "quadratic", "linear",
                "logarithm", "exponent", "radical",
                "roots", "root"
            ],

            "Calculus": [
                "calculus", "derivative", "differentiate",
                "differentiation", "integral", "integrate",
                "integration", "limit", "continuity",
                "continuous", "critical point",
                "maximum", "minimum", "monotonicity"
            ],

            "Geometry": [
                "geometry", "area", "perimeter",
                "circumference", "radius", "diameter",
                "rectangle", "square", "triangle",
                "circle", "cube", "cuboid", "cylinder",
                "cone", "sphere", "midpoint", "slope",
                "distance between points"
            ],

            "Trigonometry": [
                "trigonometry", "sine", "cosine",
                "tangent", "cotangent", "secant",
                "cosecant", "sin", "cos", "tan",
                "angle", "radians", "degrees",
                "pythagorean identity", "sine rule",
                "cosine rule"
            ]
        }

        # ====================================================
        # PROBLEM TYPE RECOGNITION
        # ====================================================

        self.problem_patterns = [

            # Algebra

            (r"difference of squares",
             "Algebra", "difference_of_squares"),

            (r"complete the square",
             "Algebra", "complete_the_square"),

            (r"quadratic.*discriminant|discriminant.*quadratic",
             "Algebra", "quadratic_discriminant"),

            (r"quadratic.*factor|factor.*quadratic",
             "Algebra", "quadratic_by_factoring"),

            (r"quadratic.*equation|solve.*quadratic",
             "Algebra", "quadratic_equation"),

            (r"linear.*system|system.*equations",
             "Algebra", "linear_system"),

            (r"absolute value.*inequality",
             "Algebra", "absolute_value_inequality"),

            (r"absolute value.*equation",
             "Algebra", "absolute_value_equation"),

            (r"linear.*inequality|inequality.*linear",
             "Algebra", "linear_inequality"),

            (r"quadratic.*inequality",
             "Algebra", "quadratic_inequality"),

            (r"logarithmic equation|log equation",
             "Algebra", "logarithmic_equation"),

            (r"exponential equation",
             "Algebra", "exponential_equation"),

            (r"rational equation",
             "Algebra", "rational_equation"),

            (r"simplify.*rational expression",
             "Algebra", "simplify_rational_expression"),

            (r"simplify.*radical|simplify.*square root",
             "Algebra", "simplify_radical"),

            (r"simplify.*exponent|laws of exponents",
             "Algebra", "simplify_exponents"),

            (r"factor.*common factor",
             "Algebra", "factor_common_factor"),

            (r"perfect square trinomial",
             "Algebra", "perfect_square_trinomial"),

            (r"expand",
             "Algebra", "expand_expression"),

            (r"factor",
             "Algebra", "factor_common_factor"),

            (r"simplify",
             "Algebra", "simplify_expression"),

            (r"polynomial.*roots|find.*roots|find.*root",
             "Algebra", "polynomial_roots"),

            (r"domain of",
             "Algebra", "algebraic_domain"),

            (r"linear equation",
             "Algebra", "linear_equation"),

            (r"equation.*fraction|fraction.*equation",
             "Algebra", "linear_equation_with_fractions"),

            (r"equation.*bracket|bracket.*equation",
             "Algebra", "linear_equation_with_brackets"),

            # General equation solving (kept after specific types)

            (r"solve\s+(?:the\s+)?equation",
             "Algebra", "linear_equation"),

            (r"find\s+(?:the\s+)?solution\s+of\s+(?:the\s+)?equation",
             "Algebra", "linear_equation"),

            # Calculus

            (r"one.?sided limit|left.?hand limit|right.?hand limit",
             "Calculus", "one_sided_limit"),

            (r"limit.*exist|exist.*limit",
             "Calculus", "limit_existence"),

            (r"continuity|continuous",
             "Calculus", "continuity"),

            (r"higher.?order derivative|second derivative|third derivative",
             "Calculus", "higher_order_derivative"),

            (r"implicit differentiation",
             "Calculus", "implicit_differentiation"),

            (r"product rule",
             "Calculus", "product_rule"),

            (r"quotient rule",
             "Calculus", "quotient_rule"),

            (r"chain rule",
             "Calculus", "chain_rule"),

            (r"trigonometric derivative|derivative.*sin|derivative.*cos",
             "Calculus", "trigonometric_derivative"),

            (r"logarithmic derivative",
             "Calculus", "logarithmic_derivative"),

            (r"exponential derivative",
             "Calculus", "exponential_derivative"),

            (r"critical points?",
             "Calculus", "critical_points"),

            (r"monotonicity|increasing.*decreasing",
             "Calculus", "monotonicity"),

            (r"local extrema|local maximum|local minimum",
             "Calculus", "local_extrema"),

            (r"fundamental theorem of calculus",
             "Calculus", "fundamental_theorem_calculus"),

            (r"definite integral",
             "Calculus", "definite_integral"),

            (r"substitution.*integration|integration.*substitution",
             "Calculus", "integration_substitution"),

            (r"trigonometric integral",
             "Calculus", "trigonometric_integral"),

            (r"indefinite integral|integrate|integration",
             "Calculus", "indefinite_integral"),

            (r"limit",
             "Calculus", "limit"),

            (r"derivative|differentiate|differentiation",
             "Calculus", "derivative"),

            # Geometry

            (r"circle.*circumference|circumference.*circle",
             "Geometry", "circle_circumference"),

            (r"circle.*area|area.*circle",
             "Geometry", "circle_area"),

            (r"circle.*diameter|diameter.*circle",
             "Geometry", "circle_diameter"),

            (r"rectangle.*perimeter|perimeter.*rectangle",
             "Geometry", "rectangle_perimeter"),

            (r"rectangle.*area|area.*rectangle",
             "Geometry", "rectangle_area"),

            (r"square.*perimeter|perimeter.*square",
             "Geometry", "square_perimeter"),

            (r"square.*area|area.*square",
             "Geometry", "square_area"),

            (r"triangle.*perimeter|perimeter.*triangle",
             "Geometry", "triangle_perimeter"),

            (r"heron",
             "Geometry", "heron_formula"),

            (r"triangle.*area|area.*triangle",
             "Geometry", "triangle_area"),

            (r"pythagorean theorem",
             "Geometry", "pythagorean_theorem"),

            (r"sector.*area|area.*sector",
             "Geometry", "sector_area"),

            (r"arc length",
             "Geometry", "arc_length"),

            (r"parallelogram.*area",
             "Geometry", "parallelogram_area"),

            (r"trapezoid.*area",
             "Geometry", "trapezoid_area"),

            (r"rhombus.*area",
             "Geometry", "rhombus_area"),

            (r"cube.*volume",
             "Geometry", "cube_volume"),

            (r"cuboid.*volume",
             "Geometry", "cuboid_volume"),

            (r"cylinder.*volume",
             "Geometry", "cylinder_volume"),

            (r"cone.*volume",
             "Geometry", "cone_volume"),

            (r"sphere.*volume",
             "Geometry", "sphere_volume"),

            (r"sphere.*surface area",
             "Geometry", "sphere_surface_area"),

            (r"distance between points|distance formula",
             "Geometry", "distance_formula"),

            (r"midpoint",
             "Geometry", "midpoint_formula"),

            (r"slope",
             "Geometry", "slope_formula"),

            # Trigonometry

            (r"degrees.*radians|degree.*radian|convert.*radian",
             "Trigonometry", "angle_conversion"),

            (r"standard angle",
             "Trigonometry", "standard_angle"),

            (r"complementary angle",
             "Trigonometry", "complementary_angle_identity"),

            (r"double angle.*sine|sine.*double angle",
             "Trigonometry", "double_angle_sine"),

            (r"double angle.*cosine|cosine.*double angle",
             "Trigonometry", "double_angle_cosine"),

            (r"sine addition",
             "Trigonometry", "sine_addition"),

            (r"cosine addition",
             "Trigonometry", "cosine_addition"),

            (r"sine rule",
             "Trigonometry", "sine_rule"),

            (r"cosine rule",
             "Trigonometry", "cosine_rule"),

            (r"triangle angle sum",
             "Trigonometry", "triangle_angle_sum"),

            (r"inverse sine|arcsin",
             "Trigonometry", "inverse_sine"),

            (r"inverse cosine|arccos",
             "Trigonometry", "inverse_cosine"),

            (r"inverse tangent|arctan",
             "Trigonometry", "inverse_tangent"),

            (r"trigonometric equation|solve.*sin|solve.*cos|solve.*tan",
             "Trigonometry", "basic_trigonometric_equation"),

            (r"trigonometric identity|pythagorean identity",
             "Trigonometry", "pythagorean_identity"),

            (r"trigonometric.*simplif|simplif.*trigonometric",
             "Trigonometry", "trigonometric_simplification"),

            (r"cosecant",
             "Trigonometry", "cosecant_ratio"),

            (r"secant",
             "Trigonometry", "secant_ratio"),

            (r"cotangent",
             "Trigonometry", "cotangent_ratio"),

            (r"\bsine\b|\bsin\s*\(",
             "Trigonometry", "sine_ratio"),

            (r"\bcosine\b|\bcos\s*\(",
             "Trigonometry", "cosine_ratio"),

            (r"\btangent\b|\btan\s*\(",
             "Trigonometry", "tangent_ratio"),

        ]

    # ========================================================
    # DOMAIN DETECTION
    # ========================================================

    def detect_domain(self, text):

        text = text.lower()

        scores = {}

        for domain, keywords in self.domain_keywords.items():

            scores[domain] = sum(
                1 for keyword in keywords
                if re.search(
                    r"\b" + re.escape(keyword) + r"\b",
                    text
                )
            )

        highest = max(scores.values())

        if highest == 0:
            return None

        winners = [
            domain for domain, score in scores.items()
            if score == highest
        ]

        if len(winners) != 1:
            return None

        return winners[0]

    # ========================================================
    # PROBLEM TYPE DETECTION
    # ========================================================

    def detect_problem_type(self, text):

        text = text.lower().strip()

        # Detect quadratic expressions using x**2 or x^2.
        has_quadratic = bool(
            re.search(r"\bx\s*(?:\*\*|\^)\s*2\b", text)
            or "quadratic" in text
        )

        solving_intent = bool(
            re.search(
                r"\b(solve|find|calculate|determine)\b",
                text
            )
        )

        root_intent = bool(
            re.search(r"\b(roots|root|solutions)\b", text)
        )

        # Quadratic recognition takes priority.
        if has_quadratic and (solving_intent or root_intent):
            return "Algebra", "quadratic_equation"

        # Use other existing patterns.
        for pattern, domain, problem_type in self.problem_patterns:

            if re.search(pattern, text):
                return domain, problem_type

        return None, None

    # ========================================================
    # MATHEMATICAL EXPRESSION EXTRACTION
    # ========================================================

    def extract_expression(self, text):

        text = text.strip()

        prefixes = [

            r"^(?:please\s+)?solve\s+(?:the\s+)?quadratic\s+equation\s*",

            r"^(?:please\s+)?solve\s+(?:the\s+)?linear\s+equation\s*",

            r"^(?:please\s+)?solve\s+(?:the\s+)?equation\s*",

            r"^(?:please\s+)?find\s+(?:the\s+)?roots\s+of\s*",

            r"^(?:please\s+)?find\s+(?:the\s+)?root\s+of\s*",

            r"^(?:please\s+)?find\s+(?:the\s+)?solution\s+of\s+(?:the\s+)?equation\s*",

            r"^(?:please\s+)?solve\s+",

            r"^(?:please\s+)?simplify\s+",

            r"^(?:please\s+)?factor\s+",

            r"^(?:please\s+)?expand\s+",

            r"^(?:please\s+)?differentiate\s+",

            r"^(?:please\s+)?integrate\s+",

        ]

        cleaned = text

        for prefix in prefixes:

            result = re.sub(
                prefix,
                "",
                cleaned,
                count=1,
                flags=re.IGNORECASE
            )

            if result != cleaned:
                cleaned = result
                break

        return cleaned.strip(" .?!") if cleaned.strip(" .?!") else None

    # ========================================================
    # MATHEMATICAL FEATURE DETECTION
    # ========================================================

    def detect_features(self, text, expression=None):

        text = text.lower()

        expression = (expression or "").lower()

        combined = text + " " + expression

        facts = set()

        # ---------------- Algebra features ----------------

        if "=" in combined:

            facts.add("equation")
            facts.add("polynomial_equation")

        if any(symbol in combined for symbol in [
            "<", ">", "<=", ">="
        ]):

            facts.add("inequality")

        if re.search(r"\b\d+/\d+\b", combined):

            facts.add("fractions")

        if "(" in combined or ")" in combined:

            facts.add("brackets")

        if re.search(r"\bx\b", combined):

            facts.update([
                "one_variable",
                "variable",
                "x_variable"
            ])

        if re.search(r"\by\b", combined):

            facts.add("y_variable")

        # Quadratic detection

        is_quadratic = bool(
            re.search(r"\bx\s*(?:\*\*|\^)\s*2\b", combined)
        )

        if is_quadratic:

            facts.update([
                "degree_two",
                "quadratic_expression",
                "polynomial",
                "power_expression"
            ])

        # Higher-degree polynomial detection

        if re.search(
            r"\bx\s*(?:\*\*|\^)\s*[3-9]\b",
            combined
        ):

            facts.update([
                "polynomial",
                "power_expression"
            ])

        # Logarithms

        if "log" in combined:

            facts.update([
                "logarithms",
                "logarithmic_expression"
            ])

        # Radicals

        if "sqrt" in combined or "square root" in combined:

            facts.update([
                "radicals",
                "radical_expression"
            ])

        # First-degree detection
        # Do not classify quadratic expressions as first-degree.

        if not is_quadratic:

            if re.search(
                r"\d+\s*\*?\s*x|x\s*\*?\s*\d+",
                combined
            ):

                facts.add("first_degree")

        # ---------------- Calculus features ----------------

        if any(word in text for word in [
            "derivative", "differentiate", "integral",
            "integrate", "limit", "continuity"
        ]):

            facts.add("function")

        if "second derivative" in text:

            facts.add("derivative_order")

        if "product rule" in text:

            facts.add("product_of_functions")

        if "quotient rule" in text:

            facts.add("quotient_of_functions")

        if "chain rule" in text:

            facts.add("composite_function")

        if any(word in combined for word in [
            "sin", "cos", "tan"
        ]):

            facts.update([
                "trigonometric_expression",
                "trigonometric_function",
                "trigonometric_terms"
            ])

        if "exp(" in combined or "exponential" in combined:

            facts.add("exponential_expression")

        if "ln(" in combined or "log(" in combined:

            facts.add("logarithmic_expression")

        # ---------------- Geometry features ----------------

        number_matches = re.findall(
            r"(?<![a-zA-Z])\d+(?:\.\d+)?",
            combined
        )

        for word in [
            "radius", "length", "width",
            "height", "base", "side"
        ]:

            if word in combined:

                facts.add(word)

        # ---------------- Trigonometry features ----------------

        if "opposite" in combined:

            facts.add("opposite_side")

        if "adjacent" in combined:

            facts.add("adjacent_side")

        if "hypotenuse" in combined:

            facts.add("hypotenuse")

        if "degree" in combined:

            facts.update([
                "angle_value",
                "source_unit"
            ])

        if "radian" in combined:

            facts.update([
                "angle_value",
                "source_unit"
            ])

        if "angle" in combined:

            facts.add("angle")

        if len(number_matches) >= 2:

            facts.add("two_known_sides")

        return sorted(facts)

    # ========================================================
    # MAIN NLP PROCESSING METHOD
    # ========================================================

    def process(self, user_text):

        if not isinstance(user_text, str) or not user_text.strip():

            return {

                "status": "invalid",

                "message": "Please enter a mathematical question.",

                "domain": None,

                "problem_type": None,

                "expression": None,

                "recognized_facts": [],

                "missing_features": []
            }

        text = user_text.strip()

        detected_domain, problem_type = (
            self.detect_problem_type(text)
        )

        keyword_domain = self.detect_domain(text)

        if detected_domain is None:

            return {

                "status": "unsupported",

                "message": (
                    "The system could not identify a supported "
                    "mathematical problem type."
                ),

                "domain": keyword_domain,

                "problem_type": None,

                "expression": self.extract_expression(text),

                "recognized_facts": self.detect_features(text),

                "missing_features": []
            }

        expression = self.extract_expression(text)

        facts = self.detect_features(text, expression)

        matching_rules = [

            rule for rule in self.rules

            if rule["domain"].lower() == detected_domain.lower()

            and rule["conditions"]["problem_type"].lower()
            == problem_type.lower()
        ]

        if not matching_rules:

            return {

                "status": "unsupported",

                "message": "No matching expert rule was found.",

                "domain": detected_domain,

                "problem_type": problem_type,

                "expression": expression,

                "recognized_facts": facts,

                "missing_features": []
            }

        best_rule = None

        best_missing = None

        for rule in matching_rules:

            required = set(
                rule["conditions"]["required_features"]
            )

            missing = sorted(required - set(facts))

            if (
                best_missing is None
                or len(missing) < len(best_missing)
            ):

                best_rule = rule

                best_missing = missing

        if best_missing:

            return {

                "status": "incomplete",

                "message": (
                    "The problem was identified, but some "
                    "required information is missing."
                ),

                "domain": detected_domain,

                "problem_type": problem_type,

                "expression": expression,

                "recognized_facts": facts,

                "missing_features": best_missing,

                "matched_rule": best_rule["id"]
            }

        return {

            "status": "recognized",

            "message": "The mathematical problem was recognized.",

            "domain": detected_domain,

            "problem_type": problem_type,

            "expression": expression,

            "recognized_facts": facts,

            "missing_features": [],

            "matched_rule": best_rule["id"]
        }


# ============================================================
# CREATE DEFAULT NLP PROCESSOR
# ============================================================

nlp_processor = MathematicsNLP()
