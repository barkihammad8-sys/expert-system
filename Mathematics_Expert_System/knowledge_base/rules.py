
# ============================================================
# INTELLIGENT MATHEMATICS EXPERT SYSTEM
# KNOWLEDGE BASE - EXPERT RULES
# ============================================================

def create_rule(
    rule_id,
    domain,
    name,
    description,
    problem_type,
    required_features,
    assertion_ids,
    action,
    verification
):
    return {
        "id": rule_id,
        "domain": domain,
        "name": name,
        "description": description,
        "conditions": {
            "problem_type": problem_type,
            "required_features": required_features
        },
        "assertions": assertion_ids,
        "action": action,
        "verification": verification
    }


# ============================================================
# ALGEBRA EXPERT RULES (25)
# ============================================================

ALGEBRA_RULES = [

    # 1. Linear equations
    create_rule(
        "ALG_R001", "Algebra",
        "Solve Linear Equation",
        "Apply algebraic operations to isolate the unknown variable.",
        "linear_equation",
        ["equation", "one_variable", "first_degree"],
        ["ALG001", "ALG016", "ALG017"],
        "solve_linear_equation",
        "substitute_solution_into_original"
    ),

    # 2. Linear equation with fractions
    create_rule(
        "ALG_R002", "Algebra",
        "Solve Linear Equation with Fractions",
        "Remove denominators using the least common denominator before solving.",
        "linear_equation_with_fractions",
        ["equation", "fractions", "one_variable"],
        ["ALG016", "ALG017", "ALG018"],
        "solve_linear_equation_with_fractions",
        "substitute_solution_into_original"
    ),

    # 3. Linear equation with brackets
    create_rule(
        "ALG_R003", "Algebra",
        "Solve Equation with Brackets",
        "Expand brackets and simplify before isolating the variable.",
        "linear_equation_with_brackets",
        ["equation", "brackets", "one_variable"],
        ["ALG002", "ALG003", "ALG016"],
        "expand_and_solve_linear",
        "substitute_solution_into_original"
    ),

    # 4. Simplify algebraic expression
    create_rule(
        "ALG_R004", "Algebra",
        "Simplify Algebraic Expression",
        "Combine like terms and simplify algebraic operations.",
        "simplify_expression",
        ["expression", "like_terms_or_operations"],
        ["ALG001", "ALG002", "ALG003"],
        "simplify_algebraic_expression",
        "verify_algebraic_equivalence"
    ),

    # 5. Expand expression
    create_rule(
        "ALG_R005", "Algebra",
        "Expand Algebraic Expression",
        "Apply the distributive property to remove brackets.",
        "expand_expression",
        ["expression", "multiplication_of_terms"],
        ["ALG002", "ALG003"],
        "expand_expression",
        "verify_algebraic_equivalence"
    ),

    # 6. Factor common factor
    create_rule(
        "ALG_R006", "Algebra",
        "Factor Out Common Factor",
        "Identify and extract the greatest common factor.",
        "factor_common_factor",
        ["polynomial", "common_factor"],
        ["ALG004", "ALG005"],
        "factor_common_factor",
        "expand_factorized_expression"
    ),

    # 7. Difference of squares
    create_rule(
        "ALG_R007", "Algebra",
        "Factor Difference of Squares",
        "Use the difference of two squares identity.",
        "difference_of_squares",
        ["polynomial", "two_square_terms", "subtraction"],
        ["ALG006"],
        "factor_difference_of_squares",
        "expand_factorized_expression"
    ),

    # 8. Perfect square trinomial
    create_rule(
        "ALG_R008", "Algebra",
        "Factor Perfect Square Trinomial",
        "Recognize and factor a perfect square trinomial.",
        "perfect_square_trinomial",
        ["quadratic_expression", "perfect_square_pattern"],
        ["ALG007", "ALG008"],
        "factor_perfect_square_trinomial",
        "expand_factorized_expression"
    ),

    # 9. General quadratic equation
    create_rule(
        "ALG_R009", "Algebra",
        "Solve Quadratic Equation",
        "Apply the quadratic formula to find the roots.",
        "quadratic_equation",
        ["equation", "degree_two", "one_variable"],
        ["ALG020", "ALG021", "ALG022"],
        "solve_quadratic_equation",
        "substitute_roots_into_original"
    ),

    # 10. Quadratic equation by factoring
    create_rule(
        "ALG_R010", "Algebra",
        "Solve Quadratic by Factoring",
        "Factor the quadratic and apply the zero-product property.",
        "quadratic_by_factoring",
        ["quadratic_equation", "factorable"],
        ["ALG006", "ALG009", "ALG020"],
        "solve_quadratic_by_factoring",
        "substitute_roots_into_original"
    ),

    # 11. Quadratic discriminant
    create_rule(
        "ALG_R011", "Algebra",
        "Analyze Quadratic Discriminant",
        "Determine the nature of quadratic roots using the discriminant.",
        "quadratic_discriminant",
        ["quadratic_equation", "coefficients_a_b_c"],
        ["ALG021", "ALG022"],
        "analyze_quadratic_discriminant",
        "verify_discriminant_classification"
    ),

    # 12. Complete the square
    create_rule(
        "ALG_R012", "Algebra",
        "Complete the Square",
        "Rewrite a quadratic expression as a perfect square plus a constant.",
        "complete_the_square",
        ["quadratic_expression", "one_variable"],
        ["ALG023", "ALG024"],
        "complete_square",
        "expand_completed_square"
    ),

    # 13. Exponent simplification
    create_rule(
        "ALG_R013", "Algebra",
        "Apply Exponent Laws",
        "Simplify powers using valid exponent rules.",
        "simplify_exponents",
        ["expression", "exponents"],
        ["ALG030", "ALG031", "ALG032"],
        "simplify_exponents",
        "verify_power_equivalence"
    ),

    # 14. Radical simplification
    create_rule(
        "ALG_R014", "Algebra",
        "Simplify Radical Expression",
        "Simplify square roots and other supported radicals.",
        "simplify_radical",
        ["expression", "radicals"],
        ["ALG033", "ALG034"],
        "simplify_radical",
        "verify_radical_equivalence"
    ),

    # 15. Rational expression
    create_rule(
        "ALG_R015", "Algebra",
        "Simplify Rational Expression",
        "Factor the numerator and denominator and cancel valid common factors.",
        "simplify_rational_expression",
        ["rational_expression", "denominator_nonzero"],
        ["ALG040", "ALG041", "ALG042"],
        "simplify_rational_expression",
        "verify_original_domain_and_equivalence"
    ),

    # 16. Rational equation
    create_rule(
        "ALG_R016", "Algebra",
        "Solve Rational Equation",
        "Clear denominators and solve while excluding invalid denominator values.",
        "rational_equation",
        ["equation", "rational_terms", "denominator_nonzero"],
        ["ALG040", "ALG041", "ALG043"],
        "solve_rational_equation",
        "substitute_and_check_denominators"
    ),

    # 17. Linear inequality
    create_rule(
        "ALG_R017", "Algebra",
        "Solve Linear Inequality",
        "Isolate the variable while preserving or reversing the inequality sign as required.",
        "linear_inequality",
        ["inequality", "one_variable", "first_degree"],
        ["ALG050", "ALG051"],
        "solve_linear_inequality",
        "verify_solution_interval"
    ),

    # 18. Quadratic inequality
    create_rule(
        "ALG_R018", "Algebra",
        "Solve Quadratic Inequality",
        "Find critical roots and analyze the sign of the quadratic expression.",
        "quadratic_inequality",
        ["inequality", "degree_two"],
        ["ALG050", "ALG052"],
        "solve_quadratic_inequality",
        "verify_solution_intervals"
    ),

    # 19. Absolute value equation
    create_rule(
        "ALG_R019", "Algebra",
        "Solve Absolute Value Equation",
        "Split an absolute value equation into its valid positive and negative cases.",
        "absolute_value_equation",
        ["equation", "absolute_value"],
        ["ALG060", "ALG061"],
        "solve_absolute_value_equation",
        "substitute_all_candidate_solutions"
    ),

    # 20. Absolute value inequality
    create_rule(
        "ALG_R020", "Algebra",
        "Solve Absolute Value Inequality",
        "Convert an absolute value inequality into equivalent interval conditions.",
        "absolute_value_inequality",
        ["inequality", "absolute_value"],
        ["ALG060", "ALG062"],
        "solve_absolute_value_inequality",
        "verify_solution_interval"
    ),

    # 21. Simultaneous linear equations
    create_rule(
        "ALG_R021", "Algebra",
        "Solve System of Linear Equations",
        "Solve a supported system using substitution or elimination.",
        "linear_system",
        ["multiple_equations", "multiple_variables"],
        ["ALG070", "ALG071", "ALG072"],
        "solve_linear_system",
        "substitute_solution_into_every_equation"
    ),

    # 22. Logarithmic equation
    create_rule(
        "ALG_R022", "Algebra",
        "Solve Logarithmic Equation",
        "Apply logarithm laws and convert between logarithmic and exponential forms.",
        "logarithmic_equation",
        ["equation", "logarithms", "positive_log_arguments"],
        ["ALG035", "ALG036", "ALG037"],
        "solve_logarithmic_equation",
        "check_logarithm_domains_and_original_equation"
    ),

    # 23. Exponential equation
    create_rule(
        "ALG_R023", "Algebra",
        "Solve Exponential Equation",
        "Use equal bases or logarithms to solve supported exponential equations.",
        "exponential_equation",
        ["equation", "variable_in_exponent"],
        ["ALG030", "ALG038", "ALG039"],
        "solve_exponential_equation",
        "substitute_solution_into_original"
    ),

    # 24. Polynomial roots
    create_rule(
        "ALG_R024", "Algebra",
        "Find Polynomial Roots",
        "Find roots of supported polynomial equations using symbolic solving.",
        "polynomial_roots",
        ["polynomial_equation", "one_variable"],
        ["ALG025", "ALG026", "ALG027"],
        "solve_polynomial_roots",
        "substitute_roots_into_original"
    ),

    # 25. Domain of algebraic expression
    create_rule(
        "ALG_R025", "Algebra",
        "Determine Algebraic Domain",
        "Identify restrictions caused by denominators and even-indexed radicals.",
        "algebraic_domain",
        ["expression", "domain_restrictions"],
        ["ALG043", "ALG044", "ALG045"],
        "determine_algebraic_domain",
        "verify_all_domain_restrictions"
    ),

]


# ============================================================
# CURRENT RULE COLLECTION
# More domains will be added in later phases.
# ============================================================


# ============================================================
# CALCULUS EXPERT RULES
# 25 RULES: CAL_R001 - CAL_R025
# ============================================================

CALCULUS_RULES = [

    create_rule(
        "CAL_R001", "Calculus",
        "Basic Limit Evaluation",
        "Evaluates a limit by direct substitution when the function is continuous at the target.",
        "limit",
        ["function", "limit_point"],
        ["CAL001", "CAL002", "CAL003"],
        "Apply direct substitution to evaluate the limit.",
        "Verify that substitution produces a defined finite value."
    ),

    create_rule(
        "CAL_R002", "Calculus",
        "Limit by Factorization",
        "Uses factorization to simplify an indeterminate limit.",
        "limit",
        ["function", "limit_point", "factorable_expression"],
        ["CAL004", "CAL005", "CAL006"],
        "Factor the expression, cancel common factors, and evaluate the simplified limit.",
        "Verify the simplified expression is equivalent near the limit point, excluding cancelled zero factors."
    ),

    create_rule(
        "CAL_R003", "Calculus",
        "Limit by Rationalization",
        "Uses a conjugate to simplify limits containing radicals.",
        "limit",
        ["function", "limit_point", "radical_expression"],
        ["CAL007", "CAL008", "CAL009"],
        "Multiply by the appropriate conjugate and simplify before evaluating.",
        "Verify the rationalized expression is equivalent on its valid domain."
    ),

    create_rule(
        "CAL_R004", "Calculus",
        "One-Sided Limits",
        "Evaluates left-hand and right-hand limits separately.",
        "one_sided_limit",
        ["function", "limit_point", "direction"],
        ["CAL010", "CAL011", "CAL012"],
        "Calculate the requested left-hand or right-hand limit.",
        "Check the direction of approach and the resulting limit."
    ),

    create_rule(
        "CAL_R005", "Calculus",
        "Limit Existence",
        "Determines whether a two-sided limit exists.",
        "limit_existence",
        ["function", "limit_point", "left_limit", "right_limit"],
        ["CAL013", "CAL014", "CAL015"],
        "Compare the left-hand and right-hand limits.",
        "A finite two-sided limit exists only when both one-sided limits are equal."
    ),

    create_rule(
        "CAL_R006", "Calculus",
        "Continuity at a Point",
        "Checks whether a function is continuous at a specified point.",
        "continuity",
        ["function", "limit_point", "function_value"],
        ["CAL016", "CAL017", "CAL018"],
        "Evaluate the function and its limit at the specified point, then compare them.",
        "Verify that the function value exists and equals the finite two-sided limit."
    ),

    create_rule(
        "CAL_R007", "Calculus",
        "Power Rule Differentiation",
        "Differentiates powers of a variable.",
        "derivative",
        ["function", "variable", "power_expression"],
        ["CAL019", "CAL020", "CAL021"],
        "Apply d(x^n)/dx = n*x^(n-1).",
        "Differentiate the result symbolically and compare it with the original derivative."
    ),

    create_rule(
        "CAL_R008", "Calculus",
        "Constant and Sum Rules",
        "Differentiates constants and sums or differences of functions.",
        "derivative",
        ["function", "variable", "sum_or_constant"],
        ["CAL022", "CAL023", "CAL024"],
        "Apply the constant rule and differentiate each term separately.",
        "Verify the derivative of every term."
    ),

    create_rule(
        "CAL_R009", "Calculus",
        "Product Rule",
        "Differentiates the product of two functions.",
        "product_rule",
        ["function", "variable", "product_of_functions"],
        ["CAL025", "CAL026", "CAL027"],
        "Apply (u*v)' = u'*v + u*v'.",
        "Verify the result using symbolic differentiation."
    ),

    create_rule(
        "CAL_R010", "Calculus",
        "Quotient Rule",
        "Differentiates a quotient of two functions.",
        "quotient_rule",
        ["function", "variable", "quotient_of_functions"],
        ["CAL028", "CAL029", "CAL030"],
        "Apply (u/v)' = (v*u' - u*v')/v^2.",
        "Verify the result and ensure the original denominator is nonzero."
    ),

    create_rule(
        "CAL_R011", "Calculus",
        "Chain Rule",
        "Differentiates composite functions.",
        "chain_rule",
        ["function", "variable", "composite_function"],
        ["CAL031", "CAL032", "CAL033"],
        "Differentiate the outer function and multiply by the derivative of the inner function.",
        "Verify the derivative using symbolic differentiation."
    ),

    create_rule(
        "CAL_R012", "Calculus",
        "Exponential Differentiation",
        "Differentiates exponential functions.",
        "exponential_derivative",
        ["function", "variable", "exponential_expression"],
        ["CAL034", "CAL035", "CAL036"],
        "Apply the appropriate exponential differentiation formula.",
        "Check the derivative using symbolic differentiation."
    ),

    create_rule(
        "CAL_R013", "Calculus",
        "Logarithmic Differentiation",
        "Differentiates logarithmic functions.",
        "logarithmic_derivative",
        ["function", "variable", "logarithmic_expression"],
        ["CAL037", "CAL038", "CAL039"],
        "Apply the logarithmic derivative formula and account for the function's domain.",
        "Verify the derivative and check that logarithm arguments satisfy their domain restrictions."
    ),

    create_rule(
        "CAL_R014", "Calculus",
        "Trigonometric Differentiation",
        "Differentiates standard trigonometric functions.",
        "trigonometric_derivative",
        ["function", "variable", "trigonometric_expression"],
        ["CAL040", "CAL041", "CAL042"],
        "Apply the standard trigonometric differentiation formulas.",
        "Verify the derivative symbolically."
    ),

    create_rule(
        "CAL_R015", "Calculus",
        "Higher-Order Derivatives",
        "Calculates second or higher-order derivatives.",
        "higher_order_derivative",
        ["function", "variable", "derivative_order"],
        ["CAL043", "CAL044", "CAL045"],
        "Differentiate the function repeatedly up to the requested order.",
        "Verify that the number of differentiations matches the requested order."
    ),

    create_rule(
        "CAL_R016", "Calculus",
        "Implicit Differentiation",
        "Differentiates equations where dependent variables are not isolated.",
        "implicit_differentiation",
        ["equation", "x_variable", "y_variable"],
        ["CAL046", "CAL047", "CAL048"],
        "Differentiate both sides with respect to x, applying the chain rule to terms involving y.",
        "Verify the differentiated equation and preserve the required dy/dx terms."
    ),

    create_rule(
        "CAL_R017", "Calculus",
        "Critical Point Identification",
        "Finds critical points using the first derivative.",
        "critical_points",
        ["function", "variable", "first_derivative"],
        ["CAL049", "CAL050", "CAL051"],
        "Solve f'(x) = 0 and identify points where the derivative does not exist while the function is defined.",
        "Check each candidate against the original function's domain."
    ),

    create_rule(
        "CAL_R018", "Calculus",
        "Increasing and Decreasing Intervals",
        "Determines intervals where a function increases or decreases.",
        "monotonicity",
        ["function", "variable", "first_derivative"],
        ["CAL052", "CAL053", "CAL054"],
        "Analyze the sign of the first derivative over the domain intervals.",
        "Verify derivative signs using valid test points."
    ),

    create_rule(
        "CAL_R019", "Calculus",
        "Local Maximum and Minimum",
        "Classifies local extrema using derivative tests.",
        "local_extrema",
        ["function", "variable", "critical_points"],
        ["CAL055", "CAL056", "CAL057"],
        "Apply the first-derivative or second-derivative test at each critical point.",
        "Confirm the classification using the applicable derivative test."
    ),

    create_rule(
        "CAL_R020", "Calculus",
        "Indefinite Integration Power Rule",
        "Integrates powers of a variable.",
        "indefinite_integral",
        ["function", "variable", "power_expression"],
        ["CAL058", "CAL059", "CAL060"],
        "Apply the power integration formula and include the constant of integration.",
        "Differentiate the antiderivative and compare it with the original integrand."
    ),

    create_rule(
        "CAL_R021", "Calculus",
        "Basic Exponential and Logarithmic Integration",
        "Integrates supported exponential and logarithmic expressions.",
        "indefinite_integral",
        ["function", "variable", "exponential_or_logarithmic"],
        ["CAL061", "CAL062", "CAL063"],
        "Apply the appropriate standard integration formula.",
        "Differentiate the proposed antiderivative to verify the integrand."
    ),

    create_rule(
        "CAL_R022", "Calculus",
        "Basic Trigonometric Integration",
        "Integrates standard trigonometric expressions.",
        "trigonometric_integral",
        ["function", "variable", "trigonometric_expression"],
        ["CAL064", "CAL065", "CAL066"],
        "Apply the appropriate standard trigonometric integration formula.",
        "Differentiate the result and verify the original integrand."
    ),

    create_rule(
        "CAL_R023", "Calculus",
        "Definite Integration",
        "Evaluates definite integrals using an antiderivative.",
        "definite_integral",
        ["function", "variable", "lower_limit", "upper_limit"],
        ["CAL067", "CAL068", "CAL069"],
        "Find an antiderivative and evaluate F(b) - F(a).",
        "Verify the antiderivative and substitute the correct integration limits."
    ),

    create_rule(
        "CAL_R024", "Calculus",
        "Integration by Substitution",
        "Uses substitution to simplify supported composite integrals.",
        "integration_substitution",
        ["function", "variable", "composite_expression", "substitution"],
        ["CAL070", "CAL071", "CAL072"],
        "Choose a suitable substitution, transform the integral, and integrate with respect to the new variable.",
        "Differentiate the resulting antiderivative and verify equivalence with the original integrand."
    ),

    create_rule(
        "CAL_R025", "Calculus",
        "Fundamental Theorem of Calculus",
        "Connects definite integration with differentiation.",
        "fundamental_theorem_calculus",
        ["function", "variable", "integration_limits"],
        ["CAL073", "CAL074", "CAL075"],
        "Apply the appropriate part of the fundamental theorem of calculus.",
        "Verify the result by differentiation or antiderivative evaluation, as applicable."
    )

]




















# ============================================================
# GEOMETRY EXPERT RULES
# 25 RULES: GEO_R001 - GEO_R025
# ============================================================

GEOMETRY_RULES = [

    create_rule(
        "GEO_R001", "Geometry",
        "Rectangle Area",
        "Calculates the area of a rectangle.",
        "rectangle_area",
        ["length", "width"],
        ["GEO001", "GEO002", "GEO003"],
        "Apply Area = length * width.",
        "Verify that length and width are positive and the result has square units."
    ),

    create_rule(
        "GEO_R002", "Geometry",
        "Rectangle Perimeter",
        "Calculates the perimeter of a rectangle.",
        "rectangle_perimeter",
        ["length", "width"],
        ["GEO004", "GEO005", "GEO006"],
        "Apply Perimeter = 2 * (length + width).",
        "Verify that both dimensions are positive and the result has linear units."
    ),

    create_rule(
        "GEO_R003", "Geometry",
        "Square Area",
        "Calculates the area of a square.",
        "square_area",
        ["side"],
        ["GEO007", "GEO008", "GEO009"],
        "Apply Area = side^2.",
        "Verify that the side length is positive."
    ),

    create_rule(
        "GEO_R004", "Geometry",
        "Square Perimeter",
        "Calculates the perimeter of a square.",
        "square_perimeter",
        ["side"],
        ["GEO010", "GEO011", "GEO012"],
        "Apply Perimeter = 4 * side.",
        "Verify that the side length is positive."
    ),

    create_rule(
        "GEO_R005", "Geometry",
        "Triangle Area",
        "Calculates the area of a triangle using its base and height.",
        "triangle_area",
        ["base", "height"],
        ["GEO013", "GEO014", "GEO015"],
        "Apply Area = (base * height) / 2.",
        "Verify that base and perpendicular height are positive."
    ),

    create_rule(
        "GEO_R006", "Geometry",
        "Triangle Perimeter",
        "Calculates the perimeter of a triangle.",
        "triangle_perimeter",
        ["side_a", "side_b", "side_c"],
        ["GEO016", "GEO017", "GEO018"],
        "Add the three side lengths.",
        "Verify that all sides are positive and satisfy the triangle inequality."
    ),

    create_rule(
        "GEO_R007", "Geometry",
        "Heron's Formula",
        "Calculates triangle area when all three side lengths are known.",
        "heron_formula",
        ["side_a", "side_b", "side_c"],
        ["GEO019", "GEO020", "GEO021"],
        "Calculate semiperimeter s = (a+b+c)/2, then area = sqrt(s*(s-a)*(s-b)*(s-c)).",
        "Verify the triangle inequality and that the expression under the square root is nonnegative."
    ),

    create_rule(
        "GEO_R008", "Geometry",
        "Pythagorean Theorem",
        "Finds a missing side of a right-angled triangle.",
        "pythagorean_theorem",
        ["two_known_sides", "right_triangle"],
        ["GEO022", "GEO023", "GEO024"],
        "Apply a^2 + b^2 = c^2, where c is the hypotenuse.",
        "Verify that the hypotenuse is the longest side and the equation is satisfied."
    ),

    create_rule(
        "GEO_R009", "Geometry",
        "Circle Area",
        "Calculates the area enclosed by a circle.",
        "circle_area",
        ["radius"],
        ["GEO025", "GEO026", "GEO027"],
        "Apply Area = pi * radius^2.",
        "Verify that the radius is positive."
    ),

    create_rule(
        "GEO_R010", "Geometry",
        "Circle Circumference",
        "Calculates the circumference of a circle.",
        "circle_circumference",
        ["radius"],
        ["GEO028", "GEO029", "GEO030"],
        "Apply Circumference = 2 * pi * radius.",
        "Verify that the radius is positive."
    ),

    create_rule(
        "GEO_R011", "Geometry",
        "Circle Diameter",
        "Calculates the diameter of a circle.",
        "circle_diameter",
        ["radius_or_diameter"],
        ["GEO031", "GEO032", "GEO033"],
        "Apply diameter = 2 * radius, or radius = diameter / 2.",
        "Verify that the supplied measurement is positive."
    ),

    create_rule(
        "GEO_R012", "Geometry",
        "Sector Area",
        "Calculates the area of a circular sector.",
        "sector_area",
        ["radius", "central_angle"],
        ["GEO034", "GEO035", "GEO036"],
        "For degrees, apply Area = (angle/360) * pi * radius^2.",
        "Verify that the radius is positive and the angle is within the supported range."
    ),

    create_rule(
        "GEO_R013", "Geometry",
        "Arc Length",
        "Calculates the length of a circular arc.",
        "arc_length",
        ["radius", "central_angle"],
        ["GEO037", "GEO038", "GEO039"],
        "For radians, apply arc length = radius * angle; convert degrees when necessary.",
        "Verify that the angle unit is identified correctly and the radius is positive."
    ),

    create_rule(
        "GEO_R014", "Geometry",
        "Parallelogram Area",
        "Calculates the area of a parallelogram.",
        "parallelogram_area",
        ["base", "height"],
        ["GEO040", "GEO041", "GEO042"],
        "Apply Area = base * perpendicular height.",
        "Verify that the base and perpendicular height are positive."
    ),

    create_rule(
        "GEO_R015", "Geometry",
        "Trapezoid Area",
        "Calculates the area of a trapezoid using its parallel sides and height.",
        "trapezoid_area",
        ["parallel_side_a", "parallel_side_b", "height"],
        ["GEO043", "GEO044", "GEO045"],
        "Apply Area = ((a+b)/2) * height.",
        "Verify that both parallel sides and the perpendicular height are positive."
    ),

    create_rule(
        "GEO_R016", "Geometry",
        "Rhombus Area",
        "Calculates the area of a rhombus using its diagonals.",
        "rhombus_area",
        ["diagonal_1", "diagonal_2"],
        ["GEO046", "GEO047", "GEO048"],
        "Apply Area = (diagonal_1 * diagonal_2) / 2.",
        "Verify that both diagonal lengths are positive."
    ),

    create_rule(
        "GEO_R017", "Geometry",
        "Cube Volume",
        "Calculates the volume of a cube.",
        "cube_volume",
        ["side"],
        ["GEO049", "GEO050", "GEO051"],
        "Apply Volume = side^3.",
        "Verify that the side length is positive."
    ),

    create_rule(
        "GEO_R018", "Geometry",
        "Cuboid Volume",
        "Calculates the volume of a cuboid.",
        "cuboid_volume",
        ["length", "width", "height"],
        ["GEO052", "GEO053", "GEO054"],
        "Apply Volume = length * width * height.",
        "Verify that all three dimensions are positive."
    ),

    create_rule(
        "GEO_R019", "Geometry",
        "Cylinder Volume",
        "Calculates the volume of a cylinder.",
        "cylinder_volume",
        ["radius", "height"],
        ["GEO055", "GEO056", "GEO057"],
        "Apply Volume = pi * radius^2 * height.",
        "Verify that radius and height are positive."
    ),

    create_rule(
        "GEO_R020", "Geometry",
        "Cone Volume",
        "Calculates the volume of a cone.",
        "cone_volume",
        ["radius", "height"],
        ["GEO058", "GEO059", "GEO060"],
        "Apply Volume = (pi * radius^2 * height) / 3.",
        "Verify that radius and height are positive."
    ),

    create_rule(
        "GEO_R021", "Geometry",
        "Sphere Volume",
        "Calculates the volume of a sphere.",
        "sphere_volume",
        ["radius"],
        ["GEO061", "GEO062", "GEO063"],
        "Apply Volume = (4/3) * pi * radius^3.",
        "Verify that the radius is positive."
    ),

    create_rule(
        "GEO_R022", "Geometry",
        "Sphere Surface Area",
        "Calculates the total surface area of a sphere.",
        "sphere_surface_area",
        ["radius"],
        ["GEO064", "GEO065", "GEO066"],
        "Apply Surface Area = 4 * pi * radius^2.",
        "Verify that the radius is positive."
    ),

    create_rule(
        "GEO_R023", "Geometry",
        "Distance Between Two Points",
        "Calculates the Euclidean distance between two coordinate points.",
        "distance_formula",
        ["point_1", "point_2"],
        ["GEO067", "GEO068", "GEO069"],
        "Apply distance = sqrt((x2-x1)^2 + (y2-y1)^2).",
        "Verify that all four coordinates are valid real numbers and the distance is nonnegative."
    ),

    create_rule(
        "GEO_R024", "Geometry",
        "Midpoint Formula",
        "Finds the midpoint of a line segment between two coordinate points.",
        "midpoint_formula",
        ["point_1", "point_2"],
        ["GEO070", "GEO071", "GEO072"],
        "Apply midpoint = ((x1+x2)/2, (y1+y2)/2).",
        "Verify that the midpoint coordinates are the averages of the corresponding endpoint coordinates."
    ),

    create_rule(
        "GEO_R025", "Geometry",
        "Slope of a Line",
        "Calculates the slope of a line through two points.",
        "slope_formula",
        ["point_1", "point_2"],
        ["GEO073", "GEO074", "GEO075"],
        "Apply slope = (y2-y1)/(x2-x1).",
        "Verify that x2 is not equal to x1; otherwise the line is vertical and its slope is undefined."
    )

]











# ============================================================
# TRIGONOMETRY EXPERT RULES
# 25 RULES: TRI_R001 - TRI_R025
# ============================================================

TRIGONOMETRY_RULES = [

    create_rule(
        "TRI_R001", "Trigonometry",
        "Sine Ratio",
        "Calculates the sine of an angle in a right-angled triangle.",
        "sine_ratio",
        ["opposite_side", "hypotenuse"],
        ["TRI001", "TRI002", "TRI003"],
        "Apply sin(theta) = opposite / hypotenuse.",
        "Verify that the hypotenuse is positive and is the longest side."
    ),

    create_rule(
        "TRI_R002", "Trigonometry",
        "Cosine Ratio",
        "Calculates the cosine of an angle in a right-angled triangle.",
        "cosine_ratio",
        ["adjacent_side", "hypotenuse"],
        ["TRI004", "TRI005", "TRI006"],
        "Apply cos(theta) = adjacent / hypotenuse.",
        "Verify that the hypotenuse is positive and the adjacent side is valid."
    ),

    create_rule(
        "TRI_R003", "Trigonometry",
        "Tangent Ratio",
        "Calculates the tangent of an angle in a right-angled triangle.",
        "tangent_ratio",
        ["opposite_side", "adjacent_side"],
        ["TRI007", "TRI008", "TRI009"],
        "Apply tan(theta) = opposite / adjacent.",
        "Verify that the adjacent side is nonzero."
    ),

    create_rule(
        "TRI_R004", "Trigonometry",
        "Cosecant Ratio",
        "Calculates the cosecant of an angle.",
        "cosecant_ratio",
        ["angle_or_sine_value"],
        ["TRI010", "TRI011", "TRI012"],
        "Apply csc(theta) = 1 / sin(theta).",
        "Verify that sin(theta) is nonzero."
    ),

    create_rule(
        "TRI_R005", "Trigonometry",
        "Secant Ratio",
        "Calculates the secant of an angle.",
        "secant_ratio",
        ["angle_or_cosine_value"],
        ["TRI013", "TRI014", "TRI015"],
        "Apply sec(theta) = 1 / cos(theta).",
        "Verify that cos(theta) is nonzero."
    ),

    create_rule(
        "TRI_R006", "Trigonometry",
        "Cotangent Ratio",
        "Calculates the cotangent of an angle.",
        "cotangent_ratio",
        ["angle_or_tangent_value"],
        ["TRI016", "TRI017", "TRI018"],
        "Apply cot(theta) = 1 / tan(theta), where defined.",
        "Verify that tan(theta) is nonzero and defined."
    ),

    create_rule(
        "TRI_R007", "Trigonometry",
        "Pythagorean Identity",
        "Uses the fundamental sine-cosine Pythagorean identity.",
        "pythagorean_identity",
        ["sine_value_or_cosine_value"],
        ["TRI019", "TRI020", "TRI021"],
        "Apply sin(theta)^2 + cos(theta)^2 = 1.",
        "Verify that the supplied values satisfy the identity."
    ),

    create_rule(
        "TRI_R008", "Trigonometry",
        "Tangent-Secant Identity",
        "Uses the Pythagorean identity involving tangent and secant.",
        "tangent_secant_identity",
        ["tangent_or_secant_value"],
        ["TRI022", "TRI023", "TRI024"],
        "Apply 1 + tan(theta)^2 = sec(theta)^2.",
        "Verify that the identity holds and all expressions are defined."
    ),

    create_rule(
        "TRI_R009", "Trigonometry",
        "Cotangent-Cosecant Identity",
        "Uses the Pythagorean identity involving cotangent and cosecant.",
        "cotangent_cosecant_identity",
        ["cotangent_or_cosecant_value"],
        ["TRI025", "TRI026", "TRI027"],
        "Apply 1 + cot(theta)^2 = csc(theta)^2.",
        "Verify that the identity holds and all expressions are defined."
    ),

    create_rule(
        "TRI_R010", "Trigonometry",
        "Complementary Angle Identities",
        "Uses cofunction identities for complementary angles.",
        "complementary_angle_identity",
        ["angle"],
        ["TRI028", "TRI029", "TRI030"],
        "Apply identities such as sin(90 degrees - theta) = cos(theta).",
        "Verify that the angle unit and complementary-angle relationship are correct."
    ),

    create_rule(
        "TRI_R011", "Trigonometry",
        "Angle Conversion",
        "Converts angles between degrees and radians.",
        "angle_conversion",
        ["angle_value", "source_unit"],
        ["TRI031", "TRI032", "TRI033"],
        "Apply radians = degrees * pi / 180, or degrees = radians * 180 / pi.",
        "Verify that the conversion uses the correct source and target units."
    ),

    create_rule(
        "TRI_R012", "Trigonometry",
        "Standard Angle Evaluation",
        "Evaluates trigonometric functions at supported standard angles.",
        "standard_angle",
        ["angle", "trigonometric_function"],
        ["TRI034", "TRI035", "TRI036"],
        "Use exact standard-angle values for the requested trigonometric function.",
        "Verify the exact value and ensure the function is defined at that angle."
    ),

    create_rule(
        "TRI_R013", "Trigonometry",
        "Sine Addition Identity",
        "Expands the sine of a sum of two angles.",
        "sine_addition",
        ["angle_a", "angle_b"],
        ["TRI037", "TRI038", "TRI039"],
        "Apply sin(A+B) = sin(A)cos(B) + cos(A)sin(B).",
        "Verify the expanded expression using symbolic trigonometric simplification."
    ),

    create_rule(
        "TRI_R014", "Trigonometry",
        "Cosine Addition Identity",
        "Expands the cosine of a sum of two angles.",
        "cosine_addition",
        ["angle_a", "angle_b"],
        ["TRI040", "TRI041", "TRI042"],
        "Apply cos(A+B) = cos(A)cos(B) - sin(A)sin(B).",
        "Verify the expanded expression using symbolic trigonometric simplification."
    ),

    create_rule(
        "TRI_R015", "Trigonometry",
        "Double Angle Sine Identity",
        "Evaluates or simplifies the sine of twice an angle.",
        "double_angle_sine",
        ["angle"],
        ["TRI043", "TRI044", "TRI045"],
        "Apply sin(2A) = 2*sin(A)*cos(A).",
        "Verify the identity symbolically."
    ),

    create_rule(
        "TRI_R016", "Trigonometry",
        "Double Angle Cosine Identity",
        "Evaluates or simplifies the cosine of twice an angle.",
        "double_angle_cosine",
        ["angle"],
        ["TRI046", "TRI047", "TRI048"],
        "Apply cos(2A) = cos(A)^2 - sin(A)^2, including equivalent forms.",
        "Verify that the selected equivalent identity is correct."
    ),

    create_rule(
        "TRI_R017", "Trigonometry",
        "Basic Trigonometric Equation",
        "Solves supported basic sine, cosine or tangent equations.",
        "basic_trigonometric_equation",
        ["equation", "variable", "trigonometric_function"],
        ["TRI049", "TRI050", "TRI051"],
        "Isolate the trigonometric function and solve using inverse functions and periodicity.",
        "Substitute candidate solutions into the original equation and respect the requested interval."
    ),

    create_rule(
        "TRI_R018", "Trigonometry",
        "Sine Rule",
        "Finds unknown sides or angles in a non-right triangle.",
        "sine_rule",
        ["side_angle_opposite_pairs"],
        ["TRI052", "TRI053", "TRI054"],
        "Apply a/sin(A) = b/sin(B) = c/sin(C).",
        "Verify that each side is paired with its opposite angle and check possible ambiguous cases."
    ),

    create_rule(
        "TRI_R019", "Trigonometry",
        "Cosine Rule",
        "Finds a missing side or angle in a non-right triangle.",
        "cosine_rule",
        ["two_sides_and_included_angle_or_three_sides"],
        ["TRI055", "TRI056", "TRI057"],
        "Apply c^2 = a^2 + b^2 - 2ab*cos(C), or its rearranged form.",
        "Verify positive side lengths and that the triangle conditions are satisfied."
    ),

    create_rule(
        "TRI_R020", "Trigonometry",
        "Triangle Angle Sum",
        "Finds a missing interior angle of a triangle.",
        "triangle_angle_sum",
        ["two_known_angles"],
        ["TRI058", "TRI059", "TRI060"],
        "Apply A + B + C = 180 degrees.",
        "Verify that all interior angles are positive and sum to 180 degrees."
    ),

    create_rule(
        "TRI_R021", "Trigonometry",
        "Inverse Sine",
        "Finds a principal angle from a sine value.",
        "inverse_sine",
        ["sine_value"],
        ["TRI061", "TRI062", "TRI063"],
        "Apply theta = arcsin(value) within the principal range.",
        "Verify that the input is between -1 and 1 and distinguish the principal angle from other periodic solutions."
    ),

    create_rule(
        "TRI_R022", "Trigonometry",
        "Inverse Cosine",
        "Finds a principal angle from a cosine value.",
        "inverse_cosine",
        ["cosine_value"],
        ["TRI064", "TRI065", "TRI066"],
        "Apply theta = arccos(value) within the principal range.",
        "Verify that the input is between -1 and 1 and distinguish the principal angle from other periodic solutions."
    ),

    create_rule(
        "TRI_R023", "Trigonometry",
        "Inverse Tangent",
        "Finds a principal angle from a tangent value.",
        "inverse_tangent",
        ["tangent_value"],
        ["TRI067", "TRI068", "TRI069"],
        "Apply theta = arctan(value) within the principal range.",
        "Verify the principal angle and distinguish it from other periodic solutions."
    ),

    create_rule(
        "TRI_R024", "Trigonometry",
        "Trigonometric Function Periodicity",
        "Uses the periodic properties of trigonometric functions.",
        "trigonometric_periodicity",
        ["function", "angle"],
        ["TRI070", "TRI071", "TRI072"],
        "Apply the correct period: 2*pi for sine and cosine, and pi for tangent.",
        "Verify the function's period and ensure the transformed expression is equivalent."
    ),

    create_rule(
        "TRI_R025", "Trigonometry",
        "Trigonometric Simplification",
        "Simplifies supported trigonometric expressions using identities.",
        "trigonometric_simplification",
        ["expression", "trigonometric_terms"],
        ["TRI073", "TRI074", "TRI075"],
        "Apply valid trigonometric identities and algebraic simplification.",
        "Verify equivalence to the original expression on the common domain of both expressions."
    )

]






# ============================================================
# COMPLETE MATHEMATICS EXPERT RULE BASE
# ============================================================

RULES = (
    ALGEBRA_RULES
    + CALCULUS_RULES
    + GEOMETRY_RULES
    + TRIGONOMETRY_RULES
)