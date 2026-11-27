
# ============================================================
# INTELLIGENT MATHEMATICS EXPERT SYSTEM
# KNOWLEDGE BASE - ALGEBRA ASSERTIONS
# ============================================================


def create_assertion(
    assertion_id,
    name,
    assertion_type,
    description,
    knowledge,
    conditions,
    domain="Algebra"
):
    return {
        "id": assertion_id,
        "domain": domain,
        "name": name,
        "type": assertion_type,
        "description": description,
        "knowledge": knowledge,
        "conditions": conditions
    }



ALGEBRA_ASSERTIONS = [

    # 1. Fundamental algebraic concepts

    create_assertion(
        "ALG001", "Linear Equation", "problem_type",
        "An equation whose highest variable power is one.",
        "ax + b = c",
        "a must not equal zero."
    ),

    create_assertion(
        "ALG002", "Quadratic Equation", "problem_type",
        "An equation whose highest variable power is two.",
        "ax^2 + bx + c = 0",
        "a must not equal zero."
    ),

    create_assertion(
        "ALG003", "Polynomial", "mathematical_concept",
        "An expression containing variables with non-negative integer powers.",
        "a_n*x^n + ... + a_1*x + a_0",
        "Variable exponents must be non-negative integers."
    ),

    create_assertion(
        "ALG004", "Monomial", "mathematical_concept",
        "An algebraic expression containing one term.",
        "5x^2",
        "A single term with a numerical coefficient and variables."
    ),

    create_assertion(
        "ALG005", "Binomial", "mathematical_concept",
        "An algebraic expression containing two unlike terms.",
        "a + b",
        "Exactly two terms."
    ),

    create_assertion(
        "ALG006", "Trinomial", "mathematical_concept",
        "An algebraic expression containing three terms.",
        "a + b + c",
        "Exactly three terms."
    ),

    create_assertion(
        "ALG007", "Coefficient", "mathematical_property",
        "A numerical factor multiplying a variable.",
        "In 7x, the coefficient is 7.",
        "Identify the numerical factor of the variable."
    ),

    create_assertion(
        "ALG008", "Constant", "mathematical_property",
        "A fixed numerical value without a variable.",
        "In 3x + 8, the constant is 8.",
        "The value does not depend on the variable."
    ),

    create_assertion(
        "ALG009", "Like Terms", "mathematical_property",
        "Terms having identical variable parts and exponents.",
        "3x + 5x = 8x",
        "Variable parts and their exponents must match."
    ),

    create_assertion(
        "ALG010", "Unlike Terms", "mathematical_property",
        "Terms having different variable parts or exponents.",
        "3x + 5x^2",
        "Unlike terms cannot be directly combined."
    ),

    # 2. Algebraic operations and properties

    create_assertion(
        "ALG011", "Commutative Addition", "algebraic_property",
        "Changing the order of addition does not change the result.",
        "a + b = b + a",
        "Applies to addition."
    ),

    create_assertion(
        "ALG012", "Commutative Multiplication", "algebraic_property",
        "Changing the order of multiplication does not change the result.",
        "a * b = b * a",
        "Applies to multiplication."
    ),

    create_assertion(
        "ALG013", "Associative Addition", "algebraic_property",
        "Changing the grouping of addition does not change the result.",
        "(a + b) + c = a + (b + c)",
        "Applies to addition."
    ),

    create_assertion(
        "ALG014", "Associative Multiplication", "algebraic_property",
        "Changing the grouping of multiplication does not change the result.",
        "(a * b) * c = a * (b * c)",
        "Applies to multiplication."
    ),

    create_assertion(
        "ALG015", "Distributive Property", "algebraic_property",
        "Multiplication distributes over addition.",
        "a(b + c) = ab + ac",
        "Multiply every term inside the parentheses."
    ),

    create_assertion(
        "ALG016", "Additive Identity", "algebraic_property",
        "Adding zero leaves a number unchanged.",
        "a + 0 = a",
        "Applies to all real numbers."
    ),

    create_assertion(
        "ALG017", "Multiplicative Identity", "algebraic_property",
        "Multiplying by one leaves a number unchanged.",
        "a * 1 = a",
        "Applies to all real numbers."
    ),

    create_assertion(
        "ALG018", "Additive Inverse", "algebraic_property",
        "A number and its opposite have a sum of zero.",
        "a + (-a) = 0",
        "The two values must be additive opposites."
    ),

    create_assertion(
        "ALG019", "Multiplicative Inverse", "algebraic_property",
        "A nonzero number multiplied by its reciprocal equals one.",
        "a * (1/a) = 1",
        "a must not equal zero."
    ),

    create_assertion(
        "ALG020", "Zero Product Property", "algebraic_property",
        "If a product equals zero, at least one factor must equal zero.",
        "ab = 0 implies a = 0 or b = 0",
        "Applies when the product is exactly zero."
    ),

    # 3. Linear equation solving

    create_assertion(
        "ALG021", "Addition Property of Equality", "solving_rule",
        "Adding the same value to both sides preserves equality.",
        "If a = b, then a + c = b + c",
        "Apply the same addition to both sides."
    ),

    create_assertion(
        "ALG022", "Subtraction Property of Equality", "solving_rule",
        "Subtracting the same value from both sides preserves equality.",
        "If a = b, then a - c = b - c",
        "Apply the same subtraction to both sides."
    ),

    create_assertion(
        "ALG023", "Multiplication Property of Equality", "solving_rule",
        "Multiplying both sides by the same value preserves equality.",
        "If a = b, then ac = bc",
        "Apply the same multiplication to both sides."
    ),

    create_assertion(
        "ALG024", "Division Property of Equality", "solving_rule",
        "Dividing both sides by the same nonzero value preserves equality.",
        "If a = b, then a/c = b/c",
        "The divisor c must not equal zero."
    ),

    create_assertion(
        "ALG025", "Linear Equation Isolation", "solving_method",
        "A variable can be isolated by applying inverse operations.",
        "ax + b = c gives x = (c-b)/a",
        "a must not equal zero."
    )
]



# ============================================================
# ALGEBRA ASSERTIONS - PART 2
# ASSERTION IDs: ALG026 - ALG050
# ============================================================

ALGEBRA_ASSERTIONS.extend([

    # 4. Factoring techniques

    create_assertion(
        "ALG026", "Common Factor", "factoring_method",
        "A common factor can be taken outside an algebraic expression.",
        "ab + ac = a(b + c)",
        "All terms must share a common factor."
    ),

    create_assertion(
        "ALG027", "Difference of Squares", "factoring_method",
        "The difference between two squares can be factored.",
        "a^2 - b^2 = (a - b)(a + b)",
        "The expression must contain a subtraction of two perfect squares."
    ),

    create_assertion(
        "ALG028", "Perfect Square Trinomial", "factoring_method",
        "A trinomial can represent the square of a binomial.",
        "a^2 + 2ab + b^2 = (a + b)^2",
        "The first and last terms must be squares and the middle term must be twice their roots' product."
    ),

    create_assertion(
        "ALG029", "Perfect Square Difference", "factoring_method",
        "A trinomial with a negative middle term can represent a squared difference.",
        "a^2 - 2ab + b^2 = (a - b)^2",
        "The first and last terms must be squares and the middle term must be negative twice their roots' product."
    ),

    create_assertion(
        "ALG030", "Quadratic Factorization", "factoring_method",
        "A quadratic expression can sometimes be expressed as two linear factors.",
        "ax^2 + bx + c = (px + q)(rx + s)",
        "The factors must expand to the original quadratic expression."
    ),

    # 5. Quadratic equations

    create_assertion(
        "ALG031", "Quadratic Formula", "solving_method",
        "The quadratic formula provides solutions to a quadratic equation.",
        "x = (-b +/- sqrt(b^2 - 4ac))/(2a)",
        "Equation must be ax^2 + bx + c = 0 with a not equal to zero."
    ),

    create_assertion(
        "ALG032", "Quadratic Discriminant", "mathematical_property",
        "The discriminant determines the nature of quadratic roots.",
        "D = b^2 - 4ac",
        "Equation must be in standard quadratic form."
    ),

    create_assertion(
        "ALG033", "Two Distinct Real Roots", "root_property",
        "A quadratic equation has two distinct real roots when its discriminant is positive.",
        "D > 0",
        "The coefficients must be real and a must not equal zero."
    ),

    create_assertion(
        "ALG034", "Repeated Real Roots", "root_property",
        "A quadratic equation has equal real roots when its discriminant is zero.",
        "D = 0",
        "The coefficients must be real and a must not equal zero."
    ),

    create_assertion(
        "ALG035", "Complex Conjugate Roots", "root_property",
        "A real-coefficient quadratic has two non-real complex conjugate roots when its discriminant is negative.",
        "D < 0",
        "The coefficients must be real and a must not equal zero."
    ),

    create_assertion(
        "ALG036", "Sum of Quadratic Roots", "root_property",
        "The sum of the roots can be calculated from the coefficients.",
        "alpha + beta = -b/a",
        "Equation must be ax^2 + bx + c = 0."
    ),

    create_assertion(
        "ALG037", "Product of Quadratic Roots", "root_property",
        "The product of the roots can be calculated from the coefficients.",
        "alpha * beta = c/a",
        "Equation must be ax^2 + bx + c = 0."
    ),

    # 6. Exponents and powers

    create_assertion(
        "ALG038", "Product Rule of Exponents", "exponent_rule",
        "Multiplying powers with the same nonzero base adds their exponents.",
        "a^m * a^n = a^(m+n)",
        "The bases must be identical."
    ),

    create_assertion(
        "ALG039", "Quotient Rule of Exponents", "exponent_rule",
        "Dividing powers with the same nonzero base subtracts their exponents.",
        "a^m / a^n = a^(m-n)",
        "The base must not be zero."
    ),

    create_assertion(
        "ALG040", "Power of a Power", "exponent_rule",
        "Raising a power to another power multiplies the exponents.",
        "(a^m)^n = a^(m*n)",
        "The bases and exponents must be valid for the number system being used."
    ),

    create_assertion(
        "ALG041", "Zero Exponent Rule", "exponent_rule",
        "Any nonzero number raised to the power zero equals one.",
        "a^0 = 1",
        "a must not equal zero."
    ),

    create_assertion(
        "ALG042", "Negative Exponent Rule", "exponent_rule",
        "A negative exponent represents the reciprocal of a positive power.",
        "a^(-n) = 1/a^n",
        "a must not equal zero."
    ),

    create_assertion(
        "ALG043", "Fractional Exponent Rule", "exponent_rule",
        "A fractional exponent can represent a root and a power.",
        "a^(1/n) = nth_root(a)",
        "For real-valued even roots, a must be non-negative; n must be positive."
    ),

    # 7. Radicals and rational expressions

    create_assertion(
        "ALG044", "Product Rule of Radicals", "radical_property",
        "The product of square roots can be combined under one square root.",
        "sqrt(a) * sqrt(b) = sqrt(a*b)",
        "For real square roots, a and b must be non-negative."
    ),

    create_assertion(
        "ALG045", "Quotient Rule of Radicals", "radical_property",
        "A quotient of square roots can be combined into one square root.",
        "sqrt(a)/sqrt(b) = sqrt(a/b)",
        "For real square roots, a must be non-negative and b must be positive."
    ),

    create_assertion(
        "ALG046", "Rational Expression", "mathematical_concept",
        "A rational expression is a quotient of two polynomials.",
        "P(x)/Q(x)",
        "The denominator Q(x) must not equal zero."
    ),

    create_assertion(
        "ALG047", "Rational Expression Simplification", "solving_method",
        "Common polynomial factors can be cancelled from numerator and denominator.",
        "A*B/(A*C) = B/C",
        "The cancelled factor A must be nonzero, and the original denominator must be nonzero."
    ),

    # 8. Algebraic inequalities

    create_assertion(
        "ALG048", "Linear Inequality", "problem_type",
        "A linear inequality compares two expressions using inequality symbols.",
        "ax + b < c",
        "For a standard linear inequality, a must not equal zero."
    ),

    create_assertion(
        "ALG049", "Positive Multiplication Inequality Rule", "solving_rule",
        "Multiplying an inequality by a positive number preserves its direction.",
        "If a < b and c > 0, then ac < bc",
        "The multiplier must be positive."
    ),

    create_assertion(
        "ALG050", "Negative Multiplication Inequality Rule", "solving_rule",
        "Multiplying an inequality by a negative number reverses its direction.",
        "If a < b and c < 0, then ac > bc",
        "The multiplier must be negative."
    )

])



# ============================================================
# ALGEBRA ASSERTIONS - PART 3
# ASSERTION IDs: ALG051 - ALG075
# ============================================================

ALGEBRA_ASSERTIONS.extend([

    # 9. Systems of linear equations

    create_assertion(
        "ALG051", "System of Linear Equations", "problem_type",
        "A collection of two or more linear equations involving common variables.",
        "a1*x + b1*y = c1; a2*x + b2*y = c2",
        "All equations must be linear in their variables."
    ),

    create_assertion(
        "ALG052", "Substitution Method", "solving_method",
        "One variable is isolated and substituted into another equation.",
        "If y = f(x), substitute f(x) for y in the other equation.",
        "The substitution must preserve the original equations."
    ),

    create_assertion(
        "ALG053", "Elimination Method", "solving_method",
        "Equations are combined to eliminate one variable.",
        "Adding or subtracting suitable multiples of equations eliminates a variable.",
        "The same operations must preserve the system's solutions."
    ),

    create_assertion(
        "ALG054", "Unique Solution of Two Linear Equations", "solution_property",
        "Two non-parallel, non-identical lines intersect at exactly one point.",
        "a1*b2 - a2*b1 != 0",
        "The equations must represent two linear equations in two variables."
    ),

    create_assertion(
        "ALG055", "No Solution of Linear System", "solution_property",
        "A system can be inconsistent when equations represent parallel distinct lines.",
        "a1/a2 = b1/b2 but a1/a2 != c1/c2",
        "The denominator coefficients used in the ratios must be nonzero."
    ),

    create_assertion(
        "ALG056", "Infinitely Many Solutions", "solution_property",
        "A dependent system represents the same line or equation.",
        "a1/a2 = b1/b2 = c1/c2",
        "The system must contain dependent equations."
    ),

    # 10. Absolute-value equations

    create_assertion(
        "ALG057", "Absolute Value", "mathematical_concept",
        "Absolute value represents the non-negative distance of a number from zero.",
        "|x| = x if x >= 0; |x| = -x if x < 0",
        "The absolute value is always non-negative."
    ),

    create_assertion(
        "ALG058", "Absolute Value Equation", "problem_type",
        "An equation involving the absolute value of an expression.",
        "|f(x)| = k",
        "If k is negative, there is no real solution; if k is non-negative, solve f(x)=k or f(x)=-k."
    ),

    create_assertion(
        "ALG059", "Absolute Value Inequality Less Than", "solving_rule",
        "An absolute value less-than inequality can be rewritten as a compound inequality.",
        "|x| < a means -a < x < a",
        "The constant a must be positive."
    ),

    create_assertion(
        "ALG060", "Absolute Value Inequality Greater Than", "solving_rule",
        "An absolute value greater-than inequality can be rewritten as two separate inequalities.",
        "|x| > a means x < -a or x > a",
        "The constant a must be non-negative."
    ),

    # 11. Rational equations

    create_assertion(
        "ALG061", "Rational Equation", "problem_type",
        "An equation containing one or more rational expressions.",
        "P(x)/Q(x) = R(x)/S(x)",
        "Every denominator must be nonzero."
    ),

    create_assertion(
        "ALG062", "Least Common Denominator", "solving_method",
        "The least common denominator can be used to eliminate fractions from an equation.",
        "Multiply every term by the LCD.",
        "The original denominators must be nonzero."
    ),

    create_assertion(
        "ALG063", "Extraneous Solution", "solution_property",
        "A candidate solution may fail to satisfy the original equation.",
        "A candidate that violates the original equation or its domain restrictions is extraneous.",
        "Substitute every candidate into the original equation."
    ),

    # 12. Logarithms

    create_assertion(
        "ALG064", "Logarithm Definition", "mathematical_concept",
        "A logarithm identifies the exponent needed to produce a given number.",
        "log_b(x) = y means b^y = x",
        "b must be positive and not equal to one; x must be positive."
    ),

    create_assertion(
        "ALG065", "Product Rule of Logarithms", "logarithm_rule",
        "The logarithm of a product is the sum of logarithms.",
        "log_b(x*y) = log_b(x) + log_b(y)",
        "The base must be positive and not equal to one; x and y must be positive."
    ),

    create_assertion(
        "ALG066", "Quotient Rule of Logarithms", "logarithm_rule",
        "The logarithm of a quotient is the difference of logarithms.",
        "log_b(x/y) = log_b(x) - log_b(y)",
        "The base must be positive and not equal to one; x and y must be positive."
    ),

    create_assertion(
        "ALG067", "Power Rule of Logarithms", "logarithm_rule",
        "An exponent inside a logarithm can be moved to the front as a multiplier.",
        "log_b(x^n) = n*log_b(x)",
        "The base must be positive and not equal to one; x must be positive for real logarithms."
    ),

    create_assertion(
        "ALG068", "Change of Base Formula", "logarithm_rule",
        "A logarithm can be evaluated using another valid logarithmic base.",
        "log_b(x) = log_c(x)/log_c(b)",
        "b and c must be positive and not equal to one; x must be positive."
    ),

    # 13. Polynomial properties

    create_assertion(
        "ALG069", "Degree of Polynomial", "mathematical_property",
        "The degree of a nonzero polynomial is the highest exponent with a nonzero coefficient.",
        "Degree = highest power of the variable",
        "The zero polynomial has no defined degree."
    ),

    create_assertion(
        "ALG070", "Factor Theorem", "polynomial_property",
        "A polynomial has factor (x - a) exactly when its value at a is zero.",
        "P(a) = 0 implies (x - a) is a factor of P(x).",
        "P(x) must be a polynomial."
    ),

    create_assertion(
        "ALG071", "Remainder Theorem", "polynomial_property",
        "The remainder when a polynomial is divided by (x - a) is P(a).",
        "Remainder = P(a)",
        "The divisor must be of the form (x - a)."
    ),

    # 14. Completing the square and verification

    create_assertion(
        "ALG072", "Completing the Square", "solving_method",
        "A quadratic expression can be rewritten as a squared binomial plus a constant.",
        "x^2 + bx = (x + b/2)^2 - (b/2)^2",
        "The coefficient of x^2 must be one; otherwise normalize first."
    ),

    create_assertion(
        "ALG073", "Quadratic Vertex Form", "mathematical_property",
        "A quadratic function can be represented using its vertex.",
        "f(x) = a(x - h)^2 + k",
        "a must not equal zero; the vertex is (h, k)."
    ),

    create_assertion(
        "ALG074", "Solution Substitution Verification", "verification_rule",
        "A proposed solution is checked by substituting it into the original equation.",
        "Evaluate LHS and RHS; a solution is valid when both are equal.",
        "Use the original equation and respect all domain restrictions."
    ),

    create_assertion(
        "ALG075", "Domain Restriction of Algebraic Expressions", "mathematical_property",
        "Some algebraic expressions are defined only for particular variable values.",
        "For P(x)/Q(x), require Q(x) != 0.",
        "Check denominator restrictions and real radical restrictions before accepting solutions."
    )

])


# Export all 75 Algebra assertions.
ASSERTIONS = ALGEBRA_ASSERTIONS






# ============================================================
# CALCULUS ASSERTIONS - PART 1
# ASSERTION IDs: CAL001 - CAL025
# ============================================================

def create_calculus_assertion(
    assertion_id,
    name,
    assertion_type,
    description,
    knowledge,
    conditions
):
    assertion = create_assertion(
        assertion_id,
        name,
        assertion_type,
        description,
        knowledge,
        conditions
    )

    assertion["domain"] = "Calculus"
    return assertion



# ============================================================
# CALCULUS ASSERTIONS - PART 1
# ASSERTION IDs: CAL001 - CAL025
# ============================================================

CALCULUS_ASSERTIONS = [

    # 1. Fundamental calculus concepts

    create_assertion(
        "CAL001", "Calculus", "mathematical_concept",
        "A branch of mathematics concerned with change and accumulation.",
        "Differential calculus studies rates of change; integral calculus studies accumulation.",
        "Identify whether a problem concerns differentiation, integration, or limits.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL002", "Limit", "mathematical_concept",
        "A limit describes the value a function approaches near a given input.",
        "lim(x->a) f(x) = L",
        "The function must approach L as x approaches a.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL003", "Left-Hand Limit", "limit_property",
        "The value a function approaches as the input approaches a from the left.",
        "lim(x->a-) f(x)",
        "Consider values of x less than a.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL004", "Right-Hand Limit", "limit_property",
        "The value a function approaches as the input approaches a from the right.",
        "lim(x->a+) f(x)",
        "Consider values of x greater than a.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL005", "Existence of Two-Sided Limit", "limit_property",
        "A two-sided limit exists when left-hand and right-hand limits are equal.",
        "lim(x->a-) f(x) = lim(x->a+) f(x)",
        "Both one-sided limits must exist and be equal.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL006", "Constant Limit Rule", "limit_rule",
        "The limit of a constant is the constant itself.",
        "lim(x->a) c = c",
        "c must be a constant.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL007", "Sum Limit Rule", "limit_rule",
        "The limit of a sum equals the sum of the limits.",
        "lim(f(x)+g(x)) = lim f(x) + lim g(x)",
        "Both individual limits must exist and be finite.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL008", "Difference Limit Rule", "limit_rule",
        "The limit of a difference equals the difference of the limits.",
        "lim(f(x)-g(x)) = lim f(x) - lim g(x)",
        "Both individual limits must exist and be finite.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL009", "Product Limit Rule", "limit_rule",
        "The limit of a product equals the product of the limits.",
        "lim(f(x)*g(x)) = lim f(x) * lim g(x)",
        "Both individual limits must exist and be finite.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL010", "Quotient Limit Rule", "limit_rule",
        "The limit of a quotient equals the quotient of the limits.",
        "lim(f(x)/g(x)) = lim f(x) / lim g(x)",
        "Both limits must exist and the denominator limit must not be zero.",
        domain="Calculus"
    ),

    # 2. Continuity

    create_assertion(
        "CAL011", "Continuity at a Point", "mathematical_property",
        "A function is continuous at a point when its limit equals its function value.",
        "lim(x->a) f(x) = f(a)",
        "The function value and two-sided limit must exist and be equal.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL012", "Continuity of Polynomial", "continuity_property",
        "Every polynomial function is continuous for all real inputs.",
        "f(x) = a_n*x^n + ... + a_0",
        "The function must be a polynomial.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL013", "Continuity of Rational Function", "continuity_property",
        "A rational function is continuous wherever its denominator is nonzero.",
        "f(x) = P(x)/Q(x)",
        "Q(x) must not equal zero.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL014", "Removable Discontinuity", "discontinuity_type",
        "A discontinuity that may be removed by redefining the function at a point.",
        "The finite two-sided limit exists, but the function value is missing or unequal.",
        "The limit must exist and be finite.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL015", "Jump Discontinuity", "discontinuity_type",
        "A discontinuity where finite left-hand and right-hand limits are different.",
        "lim(x->a-) f(x) != lim(x->a+) f(x)",
        "Both one-sided limits must exist and be finite.",
        domain="Calculus"
    ),

    # 3. Fundamental differentiation concepts

    create_assertion(
        "CAL016", "Derivative", "mathematical_concept",
        "A derivative measures the instantaneous rate of change of a function.",
        "f'(x) = lim(h->0) [f(x+h)-f(x)]/h",
        "The limit must exist and be finite for the derivative to exist.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL017", "Derivative as Slope", "derivative_property",
        "The derivative at a point gives the slope of the tangent line.",
        "Slope at x=a = f'(a)",
        "The derivative must exist at the point.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL018", "Constant Derivative Rule", "differentiation_rule",
        "The derivative of a constant is zero.",
        "d/dx(c) = 0",
        "c must be independent of x.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL019", "Power Rule", "differentiation_rule",
        "The power rule differentiates a power of the variable.",
        "d/dx(x^n) = n*x^(n-1)",
        "The expression must be a power function; handle domain restrictions where necessary.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL020", "Constant Multiple Rule", "differentiation_rule",
        "A constant multiplier remains outside the derivative.",
        "d/dx[c*f(x)] = c*f'(x)",
        "c must be constant with respect to x.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL021", "Sum Differentiation Rule", "differentiation_rule",
        "The derivative of a sum equals the sum of derivatives.",
        "d/dx[f(x)+g(x)] = f'(x)+g'(x)",
        "Both functions must be differentiable.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL022", "Difference Differentiation Rule", "differentiation_rule",
        "The derivative of a difference equals the difference of derivatives.",
        "d/dx[f(x)-g(x)] = f'(x)-g'(x)",
        "Both functions must be differentiable.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL023", "Product Rule", "differentiation_rule",
        "The derivative of a product uses the derivatives of both factors.",
        "d/dx[f(x)*g(x)] = f'(x)*g(x) + f(x)*g'(x)",
        "Both functions must be differentiable.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL024", "Quotient Rule", "differentiation_rule",
        "The derivative of a quotient is calculated using the quotient rule.",
        "d/dx[f(x)/g(x)] = [g(x)*f'(x)-f(x)*g'(x)]/g(x)^2",
        "Both functions must be differentiable and g(x) must not equal zero.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL025", "Chain Rule", "differentiation_rule",
        "The chain rule differentiates a composite function.",
        "d/dx[f(g(x))] = f'(g(x))*g'(x)",
        "The required derivatives must exist at the relevant inputs.",
        domain="Calculus"
    )
]



# ============================================================
# CALCULUS ASSERTIONS - PART 2 AND PART 3
# ASSERTION IDs: CAL026 - CAL075
# ============================================================

CALCULUS_ASSERTIONS.extend([

    # 4. Trigonometric differentiation

    create_assertion(
        "CAL026", "Sine Derivative", "differentiation_rule",
        "The derivative of sine is cosine.",
        "d/dx(sin(x)) = cos(x)",
        "The angle must be measured in radians.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL027", "Cosine Derivative", "differentiation_rule",
        "The derivative of cosine is negative sine.",
        "d/dx(cos(x)) = -sin(x)",
        "The angle must be measured in radians.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL028", "Tangent Derivative", "differentiation_rule",
        "The derivative of tangent is secant squared.",
        "d/dx(tan(x)) = sec(x)^2",
        "The original tangent function must be defined.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL029", "Cotangent Derivative", "differentiation_rule",
        "The derivative of cotangent is negative cosecant squared.",
        "d/dx(cot(x)) = -csc(x)^2",
        "The original cotangent function must be defined.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL030", "Secant Derivative", "differentiation_rule",
        "The derivative of secant is secant multiplied by tangent.",
        "d/dx(sec(x)) = sec(x)*tan(x)",
        "The original secant function must be defined.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL031", "Cosecant Derivative", "differentiation_rule",
        "The derivative of cosecant is negative cosecant multiplied by cotangent.",
        "d/dx(csc(x)) = -csc(x)*cot(x)",
        "The original cosecant function must be defined.",
        domain="Calculus"
    ),

    # 5. Exponential and logarithmic differentiation

    create_assertion(
        "CAL032", "Exponential Derivative", "differentiation_rule",
        "The derivative of the natural exponential function is itself.",
        "d/dx(e^x) = e^x",
        "The variable must be the exponent.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL033", "General Exponential Derivative", "differentiation_rule",
        "The derivative of an exponential function with constant base a includes ln(a).",
        "d/dx(a^x) = a^x*ln(a)",
        "a must be positive and not equal to one.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL034", "Natural Logarithm Derivative", "differentiation_rule",
        "The derivative of the natural logarithm is the reciprocal of its input.",
        "d/dx(ln(x)) = 1/x",
        "x must be positive for the real natural logarithm.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL035", "General Logarithm Derivative", "differentiation_rule",
        "The derivative of a logarithm with base a includes the factor 1/ln(a).",
        "d/dx(log_a(x)) = 1/(x*ln(a))",
        "x must be positive; a must be positive and not equal to one.",
        domain="Calculus"
    ),

    # 6. Advanced differentiation

    create_assertion(
        "CAL036", "Implicit Differentiation", "solving_method",
        "Differentiation can be performed when a variable is defined implicitly.",
        "Differentiate both sides with respect to x, treating y as a function of x.",
        "Apply the chain rule to terms involving y.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL037", "Second Derivative", "mathematical_concept",
        "The second derivative is the derivative of the first derivative.",
        "f''(x) = d^2f/dx^2",
        "The first derivative must be differentiable.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL038", "Higher-Order Derivative", "mathematical_concept",
        "Repeated differentiation produces higher-order derivatives.",
        "f^(n)(x) = d^n f/dx^n",
        "The required successive derivatives must exist.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL039", "Logarithmic Differentiation", "solving_method",
        "Taking logarithms can simplify differentiation of complicated products and powers.",
        "ln(y) = ln(f(x)); differentiate both sides.",
        "The logarithm must be defined on the chosen domain; handle sign and absolute value restrictions correctly.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL040", "Inverse Function Derivative", "differentiation_rule",
        "The derivative of an inverse function is related to the reciprocal of the original derivative.",
        "(f^(-1))'(y) = 1/f'(x), where y=f(x)",
        "The function must be locally invertible and f'(x) must not equal zero.",
        domain="Calculus"
    ),

    # 7. Fundamental integration concepts

    create_assertion(
        "CAL041", "Indefinite Integral", "mathematical_concept",
        "An indefinite integral represents a family of antiderivatives.",
        "Integral f(x) dx = F(x) + C",
        "F'(x) must equal f(x) on the relevant interval.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL042", "Antiderivative", "mathematical_concept",
        "An antiderivative is a function whose derivative equals the given function.",
        "F'(x) = f(x)",
        "The derivative equality must hold on the relevant interval.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL043", "Constant Integration Rule", "integration_rule",
        "The integral of a constant is the constant multiplied by the variable.",
        "Integral c dx = cx + C",
        "c must be constant with respect to x.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL044", "Power Integration Rule", "integration_rule",
        "The power rule of integration increases the exponent by one and divides by the new exponent.",
        "Integral x^n dx = x^(n+1)/(n+1) + C",
        "n must not equal -1.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL045", "Constant Multiple Integration Rule", "integration_rule",
        "A constant multiplier can be taken outside an integral.",
        "Integral c*f(x) dx = c*Integral f(x) dx",
        "c must be constant with respect to x.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL046", "Sum Integration Rule", "integration_rule",
        "The integral of a sum equals the sum of the integrals.",
        "Integral [f(x)+g(x)] dx = Integral f(x) dx + Integral g(x) dx",
        "The individual functions must be integrable on the relevant interval.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL047", "Difference Integration Rule", "integration_rule",
        "The integral of a difference equals the difference of the integrals.",
        "Integral [f(x)-g(x)] dx = Integral f(x) dx - Integral g(x) dx",
        "The individual functions must be integrable on the relevant interval.",
        domain="Calculus"
    ),

    # 8. Standard integration formulas

    create_assertion(
        "CAL048", "Exponential Integration", "integration_rule",
        "The integral of the natural exponential function is itself.",
        "Integral e^x dx = e^x + C",
        "The integration variable must be x.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL049", "General Exponential Integration", "integration_rule",
        "The integral of a^x is a^x divided by its natural logarithm.",
        "Integral a^x dx = a^x/ln(a) + C",
        "a must be positive and not equal to one.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL050", "Natural Logarithmic Integration", "integration_rule",
        "The integral of one over x is the natural logarithm of the absolute value of x.",
        "Integral 1/x dx = ln(abs(x)) + C",
        "x must not equal zero; the formula applies on intervals not crossing zero.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL051", "Sine Integration", "integration_rule",
        "The integral of sine is negative cosine.",
        "Integral sin(x) dx = -cos(x) + C",
        "The angle must be measured in radians.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL052", "Cosine Integration", "integration_rule",
        "The integral of cosine is sine.",
        "Integral cos(x) dx = sin(x) + C",
        "The angle must be measured in radians.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL053", "Secant Squared Integration", "integration_rule",
        "The integral of secant squared is tangent.",
        "Integral sec(x)^2 dx = tan(x) + C",
        "The integrand must be defined on the interval.",
        domain="Calculus"
    ),

    # 9. Integration techniques

    create_assertion(
        "CAL054", "Substitution Integration", "integration_method",
        "Substitution simplifies an integral by replacing an inner expression with a new variable.",
        "Let u = g(x), then du = g'(x) dx.",
        "The transformed integral must be correctly expressed in terms of u.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL055", "Integration by Parts", "integration_method",
        "Integration by parts transforms the integral of a product.",
        "Integral u dv = uv - Integral v du",
        "The required functions and their derivatives or antiderivatives must exist.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL056", "Partial Fraction Decomposition", "integration_method",
        "A proper rational function can be decomposed into simpler rational fractions.",
        "P(x)/Q(x) = sum of simpler partial fractions",
        "The rational function must be proper, or first undergo polynomial division; factor the denominator appropriately.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL057", "Trigonometric Integration", "integration_method",
        "Trigonometric identities can simplify integrals involving trigonometric functions.",
        "Use identities such as sin^2(x)+cos^2(x)=1.",
        "Choose an identity appropriate to the integrand.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL058", "Trigonometric Substitution", "integration_method",
        "Trigonometric substitutions can simplify certain radical expressions.",
        "Examples: x=a*sin(theta), x=a*tan(theta), x=a*sec(theta).",
        "Select a substitution matching the radical form and respect its domain.",
        domain="Calculus"
    ),

    # 10. Definite integration and calculus theorem

    create_assertion(
        "CAL059", "Definite Integral", "mathematical_concept",
        "A definite integral calculates the signed accumulation over an interval.",
        "Integral from a to b of f(x) dx",
        "The function must be integrable on the interval.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL060", "Evaluation of Definite Integral", "solving_method",
        "A definite integral can be evaluated using an antiderivative.",
        "Integral from a to b of f(x) dx = F(b)-F(a)",
        "F must be an antiderivative of f and the Fundamental Theorem conditions must hold.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL061", "Fundamental Theorem of Calculus Part One", "calculus_theorem",
        "Differentiating an accumulation function recovers its integrand.",
        "d/dx[Integral from a to x of f(t) dt] = f(x)",
        "f must be continuous at x.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL062", "Fundamental Theorem of Calculus Part Two", "calculus_theorem",
        "Definite integrals can be evaluated using an antiderivative.",
        "Integral from a to b of f(x) dx = F(b)-F(a)",
        "F must be an antiderivative of f and f must satisfy the relevant integrability conditions.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL063", "Reversal of Integration Limits", "integration_property",
        "Reversing the limits of a definite integral changes its sign.",
        "Integral from a to b of f(x) dx = - Integral from b to a of f(x) dx",
        "The integral must exist.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL064", "Zero-Width Definite Integral", "integration_property",
        "A definite integral with identical upper and lower limits is zero.",
        "Integral from a to a of f(x) dx = 0",
        "The function must be defined and integrable at the interval.",
        domain="Calculus"
    ),

    # 11. Applications of differentiation

    create_assertion(
        "CAL065", "Critical Point", "mathematical_concept",
        "A critical point occurs where the derivative is zero or does not exist at a point in the domain.",
        "f'(x) = 0 or f'(x) does not exist",
        "The point must belong to the function's domain.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL066", "Increasing Function", "mathematical_property",
        "A differentiable function is increasing on an interval when its derivative is positive throughout that interval.",
        "f'(x) > 0",
        "The derivative must be positive throughout the interval.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL067", "Decreasing Function", "mathematical_property",
        "A differentiable function is decreasing on an interval when its derivative is negative throughout that interval.",
        "f'(x) < 0",
        "The derivative must be negative throughout the interval.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL068", "First Derivative Test", "solving_method",
        "The sign change of the first derivative determines local maxima and minima.",
        "Positive to negative indicates a local maximum; negative to positive indicates a local minimum.",
        "Check derivative signs on both sides of the critical point.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL069", "Second Derivative Test", "solving_method",
        "The second derivative can classify a stationary point.",
        "If f'(a)=0 and f''(a)>0, local minimum; if f''(a)<0, local maximum.",
        "If f''(a)=0, the test is inconclusive.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL070", "Concave Up Function", "mathematical_property",
        "A twice-differentiable function is concave upward where its second derivative is positive.",
        "f''(x) > 0",
        "The second derivative must be positive throughout the interval.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL071", "Concave Down Function", "mathematical_property",
        "A twice-differentiable function is concave downward where its second derivative is negative.",
        "f''(x) < 0",
        "The second derivative must be negative throughout the interval.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL072", "Inflection Point", "mathematical_property",
        "An inflection point is a point where the function changes concavity.",
        "The concavity changes across the point.",
        "A zero second derivative alone is not sufficient; verify an actual concavity change.",
        domain="Calculus"
    ),

    # 12. Applications of integration and verification

    create_assertion(
        "CAL073", "Area Under a Curve", "application",
        "A definite integral can represent signed area between a curve and the x-axis.",
        "Area = Integral from a to b of f(x) dx",
        "For geometric area, account for regions below the x-axis by using absolute values or splitting the interval.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL074", "Area Between Two Curves", "application",
        "The area between two curves can be calculated by integrating their difference.",
        "Area = Integral from a to b of [upper function - lower function] dx",
        "Identify intersection points and ensure the upper and lower functions are correctly ordered on each interval.",
        domain="Calculus"
    ),

    create_assertion(
        "CAL075", "Calculus Solution Verification", "verification_rule",
        "A proposed derivative or antiderivative can be verified by differentiation.",
        "Differentiate the proposed antiderivative and compare it with the original integrand.",
        "The expressions must be mathematically equivalent on their common domain.",
        domain="Calculus"
    )

])



# ============================================================
# GEOMETRY ASSERTIONS
# ASSERTION IDs: GEO001 - GEO075
# ============================================================

GEOMETRY_ASSERTIONS = [

    # 1. Fundamental geometric concepts

    create_assertion(
        "GEO001", "Point", "geometric_concept",
        "A point represents an exact position in space.",
        "A point has no length, width, or height.",
        "Represented by a location or coordinate.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO002", "Line", "geometric_concept",
        "A line extends infinitely in both directions.",
        "A line has length but no thickness.",
        "Two distinct points determine exactly one line.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO003", "Line Segment", "geometric_concept",
        "A line segment is a part of a line bounded by two endpoints.",
        "Length AB = distance between endpoints A and B.",
        "Both endpoints must be identified.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO004", "Ray", "geometric_concept",
        "A ray begins at one endpoint and extends infinitely in one direction.",
        "A ray has one endpoint and one direction.",
        "The endpoint must be identified.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO005", "Plane", "geometric_concept",
        "A plane is a flat two-dimensional surface extending infinitely.",
        "A plane has length and width but no thickness.",
        "Three non-collinear points determine a plane.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO006", "Parallel Lines", "geometric_property",
        "Parallel lines lie in the same plane and never intersect.",
        "Their perpendicular distance remains constant.",
        "Both lines must lie in the same plane.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO007", "Perpendicular Lines", "geometric_property",
        "Perpendicular lines intersect at a right angle.",
        "Angle = 90 degrees.",
        "The lines must intersect at a right angle.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO008", "Intersecting Lines", "geometric_property",
        "Intersecting lines share a common point.",
        "Two non-identical lines intersect at one point in a plane.",
        "The lines must not be parallel or identical.",
        domain="Geometry"
    ),

    # 2. Angles and their properties

    create_assertion(
        "GEO009", "Acute Angle", "angle_type",
        "An acute angle measures less than 90 degrees.",
        "0 < angle < 90 degrees.",
        "The angle must be greater than zero.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO010", "Right Angle", "angle_type",
        "A right angle measures exactly 90 degrees.",
        "Angle = 90 degrees.",
        "The two rays must be perpendicular.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO011", "Obtuse Angle", "angle_type",
        "An obtuse angle measures more than 90 but less than 180 degrees.",
        "90 < angle < 180 degrees.",
        "The angle must be within the specified range.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO012", "Straight Angle", "angle_type",
        "A straight angle measures exactly 180 degrees.",
        "Angle = 180 degrees.",
        "The rays must point in opposite directions.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO013", "Reflex Angle", "angle_type",
        "A reflex angle measures more than 180 but less than 360 degrees.",
        "180 < angle < 360 degrees.",
        "The angle must be within the specified range.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO014", "Complementary Angles", "angle_property",
        "Two angles are complementary when their measures add to 90 degrees.",
        "A + B = 90 degrees.",
        "Both angles must be positive.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO015", "Supplementary Angles", "angle_property",
        "Two angles are supplementary when their measures add to 180 degrees.",
        "A + B = 180 degrees.",
        "The sum of the two angle measures must equal 180 degrees.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO016", "Vertically Opposite Angles", "angle_property",
        "Vertically opposite angles are equal when two lines intersect.",
        "Angle 1 = Angle 2.",
        "The angles must form an opposite pair at an intersection.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO017", "Linear Pair", "angle_property",
        "Adjacent angles forming a straight line have a sum of 180 degrees.",
        "A + B = 180 degrees.",
        "The two angles must be adjacent and form a straight line.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO018", "Angles Around a Point", "angle_property",
        "The sum of angles around a point is 360 degrees.",
        "A1 + A2 + ... + An = 360 degrees.",
        "The angles must complete one full rotation.",
        domain="Geometry"
    ),

    # 3. Triangles

    create_assertion(
        "GEO019", "Triangle", "geometric_concept",
        "A triangle is a polygon with three sides and three interior angles.",
        "A + B + C = 180 degrees.",
        "Three vertices must not be collinear.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO020", "Equilateral Triangle", "triangle_type",
        "An equilateral triangle has three equal sides and three equal angles.",
        "Each interior angle = 60 degrees.",
        "All three side lengths must be equal.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO021", "Isosceles Triangle", "triangle_type",
        "An isosceles triangle has at least two equal sides.",
        "Angles opposite equal sides are equal.",
        "At least two side lengths must be equal.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO022", "Scalene Triangle", "triangle_type",
        "A scalene triangle has three unequal side lengths.",
        "All three sides have different lengths.",
        "The triangle inequality must hold.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO023", "Right Triangle", "triangle_type",
        "A right triangle contains one 90-degree angle.",
        "One interior angle = 90 degrees.",
        "The triangle must satisfy the angle sum property.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO024", "Acute Triangle", "triangle_type",
        "An acute triangle has all three interior angles less than 90 degrees.",
        "A < 90, B < 90, C < 90 degrees.",
        "All three interior angles must sum to 180 degrees.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO025", "Obtuse Triangle", "triangle_type",
        "An obtuse triangle contains exactly one angle greater than 90 degrees.",
        "One angle is greater than 90 and less than 180 degrees.",
        "A triangle cannot have more than one obtuse interior angle.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO026", "Triangle Inequality Theorem", "geometric_property",
        "The sum of any two side lengths of a triangle must exceed the third side.",
        "a+b>c; a+c>b; b+c>a.",
        "All side lengths must be positive.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO027", "Triangle Perimeter", "geometry_formula",
        "The perimeter of a triangle is the sum of its three side lengths.",
        "P = a+b+c",
        "All three side lengths must be known.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO028", "Triangle Area", "geometry_formula",
        "The area of a triangle is half its base multiplied by its perpendicular height.",
        "A = (1/2)*base*height",
        "The height must be perpendicular to the selected base.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO029", "Heron's Formula", "geometry_formula",
        "Heron's formula calculates triangle area using its three side lengths.",
        "s=(a+b+c)/2; A=sqrt(s*(s-a)*(s-b)*(s-c))",
        "The three side lengths must form a valid triangle.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO030", "Triangle Exterior Angle Theorem", "geometric_property",
        "An exterior angle of a triangle equals the sum of its two opposite interior angles.",
        "Exterior angle = A+B.",
        "A and B are the two non-adjacent interior angles.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO031", "Pythagorean Theorem", "geometric_theorem",
        "The square of the hypotenuse equals the sum of the squares of the other two sides.",
        "c^2 = a^2+b^2",
        "The triangle must be a right triangle and c must be the hypotenuse.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO032", "Triangle Similarity", "geometric_property",
        "Similar triangles have equal corresponding angles and proportional corresponding sides.",
        "a1/a2 = b1/b2 = c1/c2",
        "Corresponding vertices and sides must be correctly matched.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO033", "Triangle Congruence", "geometric_property",
        "Congruent triangles have equal corresponding sides and angles.",
        "Corresponding side lengths and angle measures are equal.",
        "A valid congruence criterion such as SSS, SAS, ASA, or AAS must be established.",
        domain="Geometry"
    ),

    # 4. Quadrilaterals and polygons

    create_assertion(
        "GEO034", "Quadrilateral", "geometric_concept",
        "A quadrilateral is a polygon with four sides.",
        "Interior angle sum = 360 degrees.",
        "The quadrilateral must be a simple four-sided polygon.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO035", "Square", "quadrilateral_type",
        "A square has four equal sides and four right angles.",
        "Area = s^2; Perimeter = 4s.",
        "All sides must be equal and each angle must be 90 degrees.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO036", "Rectangle", "quadrilateral_type",
        "A rectangle has four right angles and opposite sides equal.",
        "Area = length*width; Perimeter = 2(length+width).",
        "Length and width must be positive.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO037", "Parallelogram", "quadrilateral_type",
        "A parallelogram has two pairs of opposite parallel sides.",
        "Area = base*height.",
        "Opposite sides must be parallel.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO038", "Rhombus", "quadrilateral_type",
        "A rhombus has four equal sides and opposite angles equal.",
        "Area = (1/2)*d1*d2.",
        "The diagonals must be the actual perpendicular or non-perpendicular diagonals; this area formula works for any rhombus.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO039", "Trapezoid", "quadrilateral_type",
        "A trapezoid has at least one pair of parallel opposite sides.",
        "Area = (1/2)*(a+b)*height.",
        "a and b are the lengths of the parallel sides.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO040", "Kite", "quadrilateral_type",
        "A kite is a quadrilateral with two pairs of adjacent equal sides.",
        "Area = (1/2)*d1*d2.",
        "The diagonals must be measured correctly.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO041", "Interior Angle Sum of Polygon", "geometric_property",
        "The sum of interior angles of a simple n-sided polygon is determined by its number of sides.",
        "Sum = (n-2)*180 degrees.",
        "n must be an integer greater than or equal to 3.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO042", "Exterior Angle Sum of Polygon", "geometric_property",
        "The sum of one exterior angle at each vertex of a simple convex polygon is 360 degrees.",
        "Exterior angle sum = 360 degrees.",
        "Take one consistently oriented exterior angle at each vertex.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO043", "Regular Polygon Interior Angle", "geometry_formula",
        "Each interior angle of a regular polygon can be calculated using its number of sides.",
        "Each angle = ((n-2)*180)/n degrees.",
        "The polygon must be regular and n must be at least 3.",
        domain="Geometry"
    ),

    # 5. Circles

    create_assertion(
        "GEO044", "Circle", "geometric_concept",
        "A circle consists of all points in a plane at a fixed distance from its center.",
        "(x-h)^2+(y-k)^2=r^2",
        "The radius r must be positive.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO045", "Circle Radius", "geometric_property",
        "The radius is the distance from the center to a point on the circle.",
        "r = d/2",
        "The diameter must be positive.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO046", "Circle Diameter", "geometric_property",
        "The diameter is a chord passing through the center of a circle.",
        "d = 2r",
        "The radius must be known.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO047", "Circumference of Circle", "geometry_formula",
        "The circumference is the total distance around a circle.",
        "C = 2*pi*r = pi*d",
        "The radius or diameter must be positive.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO048", "Area of Circle", "geometry_formula",
        "The area of a circle is calculated using its radius.",
        "A = pi*r^2",
        "The radius must be positive.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO049", "Arc Length", "geometry_formula",
        "Arc length is the length of a portion of a circle's circumference.",
        "L = r*theta",
        "Theta must be measured in radians and r must be positive.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO050", "Sector Area", "geometry_formula",
        "A sector is a region enclosed by two radii and an arc.",
        "A = (1/2)*r^2*theta",
        "Theta must be measured in radians and r must be positive.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO051", "Chord", "geometric_property",
        "A chord is a line segment joining two points on a circle.",
        "A diameter is the longest chord of a circle.",
        "Both endpoints must lie on the circle.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO052", "Tangent to Circle", "geometric_property",
        "A tangent touches a circle at exactly one point.",
        "The tangent is perpendicular to the radius at the contact point.",
        "The radius must end at the point of tangency.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO053", "Inscribed Angle Theorem", "geometric_theorem",
        "An inscribed angle equals half the measure of its intercepted arc.",
        "Inscribed angle = (1/2)*intercepted arc.",
        "The vertex must lie on the circle.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO054", "Central Angle", "geometric_property",
        "A central angle has its vertex at the center of a circle.",
        "Central angle = intercepted arc measure.",
        "The angle must be measured at the circle's center.",
        domain="Geometry"
    ),

    # 6. Surface area and volume

    create_assertion(
        "GEO055", "Cube Volume", "geometry_formula",
        "The volume of a cube is the cube of its side length.",
        "V = s^3",
        "The side length must be positive.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO056", "Cube Surface Area", "geometry_formula",
        "The total surface area of a cube is six times the area of one face.",
        "SA = 6s^2",
        "The side length must be positive.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO057", "Cuboid Volume", "geometry_formula",
        "The volume of a cuboid is the product of its three dimensions.",
        "V = length*width*height",
        "All dimensions must be positive.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO058", "Cuboid Surface Area", "geometry_formula",
        "The total surface area of a cuboid is the sum of the areas of its six faces.",
        "SA = 2(lw+lh+wh)",
        "All dimensions must be positive.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO059", "Cylinder Volume", "geometry_formula",
        "The volume of a cylinder equals its circular base area multiplied by height.",
        "V = pi*r^2*h",
        "Radius and height must be positive.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO060", "Cylinder Total Surface Area", "geometry_formula",
        "The total surface area includes both circular bases and the curved surface.",
        "SA = 2*pi*r*(r+h)",
        "Radius and height must be positive.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO061", "Cone Volume", "geometry_formula",
        "The volume of a cone is one-third of its base area multiplied by its height.",
        "V = (1/3)*pi*r^2*h",
        "Radius and perpendicular height must be positive.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO062", "Sphere Volume", "geometry_formula",
        "The volume of a sphere is four-thirds pi times its radius cubed.",
        "V = (4/3)*pi*r^3",
        "The radius must be positive.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO063", "Sphere Surface Area", "geometry_formula",
        "The surface area of a sphere is four times pi times the radius squared.",
        "SA = 4*pi*r^2",
        "The radius must be positive.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO064", "Pyramid Volume", "geometry_formula",
        "The volume of a pyramid is one-third of its base area multiplied by its perpendicular height.",
        "V = (1/3)*base_area*height",
        "The perpendicular height and base area must be positive.",
        domain="Geometry"
    ),

    # 7. Coordinate geometry

    create_assertion(
        "GEO065", "Distance Formula", "coordinate_geometry",
        "The distance between two points is calculated using the Pythagorean theorem.",
        "d = sqrt((x2-x1)^2+(y2-y1)^2)",
        "Both points must have valid coordinates in the same coordinate system.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO066", "Midpoint Formula", "coordinate_geometry",
        "The midpoint is the point halfway between two endpoints.",
        "M = ((x1+x2)/2, (y1+y2)/2)",
        "Both endpoint coordinates must be known.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO067", "Slope of a Line", "coordinate_geometry",
        "Slope measures the vertical change divided by horizontal change.",
        "m = (y2-y1)/(x2-x1)",
        "The x-coordinates must be different.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO068", "Slope-Intercept Form", "coordinate_geometry",
        "A non-vertical straight line can be expressed using its slope and y-intercept.",
        "y = mx+b",
        "The line must not be vertical.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO069", "Equation of a Circle", "coordinate_geometry",
        "The standard equation of a circle represents points at a fixed radius from its center.",
        "(x-h)^2+(y-k)^2=r^2",
        "The radius must be positive and (h,k) is the center.",
        domain="Geometry"
    ),

    # 8. Transformations and verification

    create_assertion(
        "GEO070", "Translation", "geometric_transformation",
        "Translation moves every point by the same horizontal and vertical displacement.",
        "(x,y) -> (x+a,y+b)",
        "The same displacement must be applied to every point.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO071", "Reflection", "geometric_transformation",
        "Reflection creates a mirror image across a specified line.",
        "Reflection across x-axis: (x,y) -> (x,-y).",
        "The reflection axis must be identified.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO072", "Rotation", "geometric_transformation",
        "Rotation turns a figure around a fixed center by a specified angle.",
        "For origin rotation by theta: (x,y) -> (x*cos(theta)-y*sin(theta), x*sin(theta)+y*cos(theta)).",
        "Theta must be measured consistently; the rotation center must be specified.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO073", "Dilation", "geometric_transformation",
        "Dilation changes the size of a figure using a scale factor.",
        "About origin: (x,y) -> (k*x,k*y).",
        "The scale factor k must be specified; k=0 collapses the figure.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO074", "Geometric Unit Consistency", "verification_rule",
        "Geometric calculations must use compatible measurement units.",
        "Area uses square units; volume uses cubic units; length uses linear units.",
        "Convert measurements to compatible units before calculation.",
        domain="Geometry"
    ),

    create_assertion(
        "GEO075", "Geometry Solution Verification", "verification_rule",
        "A geometric result should be checked against the relevant formulas and geometric conditions.",
        "Verify calculated lengths, angles, areas, and volumes against the original constraints.",
        "Check positivity, triangle inequalities, angle sums, dimensions, and units where applicable.",
        domain="Geometry"
    )

]



TRIGONOMETRY_ASSERTIONS = [

    # ---------------------------------------------------------
    # A. ANGLES AND ANGLE MEASUREMENT
    # ---------------------------------------------------------

    create_assertion(
        "TRI001", "Angle Measurement", "concept",
        "An angle measures the rotation between two rays sharing a common endpoint.",
        "Angles can be measured in degrees or radians.",
        ["Two rays share a common endpoint."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI002", "Degree to Radian Conversion", "formula",
        "Converts an angle measured in degrees into radians.",
        "radians = degrees * pi / 180",
        ["Angle is measured in degrees."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI003", "Radian to Degree Conversion", "formula",
        "Converts an angle measured in radians into degrees.",
        "degrees = radians * 180 / pi",
        ["Angle is measured in radians."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI004", "Full Rotation", "property",
        "A complete revolution around a point represents 360 degrees or 2*pi radians.",
        "360 degrees = 2*pi radians",
        ["One complete rotation is considered."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI005", "Positive and Negative Angles", "concept",
        "Positive angles are measured counterclockwise and negative angles clockwise.",
        "The sign of an angle indicates its direction of rotation.",
        ["An oriented angle is given."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI006", "Coterminal Angles", "formula",
        "Coterminal angles have the same initial and terminal sides.",
        "theta + 360*n degrees, or theta + 2*pi*n radians",
        ["n is an integer."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI007", "Reference Angle", "property",
        "A reference angle is the positive acute angle formed between the terminal side and the x-axis.",
        "Reference angle depends on the quadrant of the terminal side.",
        ["The angle is not on an axis."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI008", "Unit Circle", "concept",
        "A unit circle is a circle centered at the origin with radius one.",
        "x^2 + y^2 = 1",
        ["The coordinate system is Cartesian."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI009", "Quadrant Signs", "property",
        "The signs of trigonometric functions depend on the quadrant.",
        "Quadrant I: all positive; II: sine positive; III: tangent positive; IV: cosine positive.",
        ["The terminal side lies inside a quadrant."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI010", "Arc Length", "formula",
        "Arc length is the distance along a circular arc.",
        "s = r * theta",
        ["Radius is positive.", "Theta is measured in radians."],
        domain="Trigonometry"
    ),

    # ---------------------------------------------------------
    # B. BASIC TRIGONOMETRIC RATIOS
    # ---------------------------------------------------------

    create_assertion(
        "TRI011", "Sine Ratio", "formula",
        "Sine of an acute angle in a right triangle is opposite side divided by hypotenuse.",
        "sin(theta) = opposite / hypotenuse",
        ["Triangle is right-angled.", "Hypotenuse is nonzero."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI012", "Cosine Ratio", "formula",
        "Cosine of an acute angle in a right triangle is adjacent side divided by hypotenuse.",
        "cos(theta) = adjacent / hypotenuse",
        ["Triangle is right-angled.", "Hypotenuse is nonzero."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI013", "Tangent Ratio", "formula",
        "Tangent of an acute angle in a right triangle is opposite side divided by adjacent side.",
        "tan(theta) = opposite / adjacent",
        ["Triangle is right-angled.", "Adjacent side is nonzero."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI014", "Cosecant Ratio", "formula",
        "Cosecant is the reciprocal of sine.",
        "csc(theta) = 1 / sin(theta)",
        ["sin(theta) is not zero."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI015", "Secant Ratio", "formula",
        "Secant is the reciprocal of cosine.",
        "sec(theta) = 1 / cos(theta)",
        ["cos(theta) is not zero."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI016", "Cotangent Ratio", "formula",
        "Cotangent is the reciprocal of tangent.",
        "cot(theta) = 1 / tan(theta)",
        ["tan(theta) is defined and nonzero."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI017", "Tangent Quotient Identity", "identity",
        "Tangent can be expressed as the quotient of sine and cosine.",
        "tan(theta) = sin(theta) / cos(theta)",
        ["cos(theta) is not zero."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI018", "Cotangent Quotient Identity", "identity",
        "Cotangent can be expressed as the quotient of cosine and sine.",
        "cot(theta) = cos(theta) / sin(theta)",
        ["sin(theta) is not zero."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI019", "Reciprocal Identity for Sine", "identity",
        "Sine and cosecant are reciprocal functions.",
        "sin(theta) * csc(theta) = 1",
        ["sin(theta) is not zero."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI020", "Reciprocal Identity for Cosine", "identity",
        "Cosine and secant are reciprocal functions.",
        "cos(theta) * sec(theta) = 1",
        ["cos(theta) is not zero."],
        domain="Trigonometry"
    ),

    # ---------------------------------------------------------
    # C. FUNDAMENTAL TRIGONOMETRIC IDENTITIES
    # ---------------------------------------------------------

    create_assertion(
        "TRI021", "Pythagorean Sine Cosine Identity", "identity",
        "The sum of squared sine and cosine of an angle equals one.",
        "sin(theta)^2 + cos(theta)^2 = 1",
        ["Both functions are evaluated at the same angle."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI022", "Pythagorean Tangent Secant Identity", "identity",
        "One plus squared tangent equals squared secant.",
        "1 + tan(theta)^2 = sec(theta)^2",
        ["cos(theta) is not zero."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI023", "Pythagorean Cotangent Cosecant Identity", "identity",
        "One plus squared cotangent equals squared cosecant.",
        "1 + cot(theta)^2 = csc(theta)^2",
        ["sin(theta) is not zero."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI024", "Even Function Identity", "property",
        "Cosine and secant are even trigonometric functions.",
        "cos(-theta) = cos(theta); sec(-theta) = sec(theta)",
        ["The functions are defined at the given angle."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI025", "Odd Function Identity", "property",
        "Sine, tangent, cosecant, and cotangent are odd functions.",
        "sin(-theta) = -sin(theta); tan(-theta) = -tan(theta)",
        ["The functions are defined at the given angle."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI026", "Sine Periodicity", "property",
        "Sine repeats its values after every 2*pi radians.",
        "sin(theta + 2*pi) = sin(theta)",
        ["Angles are measured in radians."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI027", "Cosine Periodicity", "property",
        "Cosine repeats its values after every 2*pi radians.",
        "cos(theta + 2*pi) = cos(theta)",
        ["Angles are measured in radians."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI028", "Tangent Periodicity", "property",
        "Tangent repeats its values after every pi radians.",
        "tan(theta + pi) = tan(theta)",
        ["Both sides are defined."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI029", "Cofunction Identity", "identity",
        "Sine of an angle equals cosine of its complementary angle.",
        "sin(theta) = cos(pi/2 - theta)",
        ["Angles are measured in radians."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI030", "Cosine Difference Identity", "identity",
        "Cosine of an angle difference can be expanded using sine and cosine.",
        "cos(A - B) = cos(A)*cos(B) + sin(A)*sin(B)",
        ["A and B are real angles."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI031", "Cosine Sum Identity", "identity",
        "Cosine of an angle sum can be expanded using sine and cosine.",
        "cos(A + B) = cos(A)*cos(B) - sin(A)*sin(B)",
        ["A and B are real angles."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI032", "Sine Sum Identity", "identity",
        "Sine of an angle sum can be expanded using sine and cosine.",
        "sin(A + B) = sin(A)*cos(B) + cos(A)*sin(B)",
        ["A and B are real angles."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI033", "Sine Difference Identity", "identity",
        "Sine of an angle difference can be expanded using sine and cosine.",
        "sin(A - B) = sin(A)*cos(B) - cos(A)*sin(B)",
        ["A and B are real angles."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI034", "Tangent Sum Identity", "identity",
        "Tangent of a sum can be expressed as a fraction.",
        "tan(A + B) = (tan(A) + tan(B)) / (1 - tan(A)*tan(B))",
        ["Both tangent values are defined.", "Denominator is not zero."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI035", "Tangent Difference Identity", "identity",
        "Tangent of a difference can be expressed as a fraction.",
        "tan(A - B) = (tan(A) - tan(B)) / (1 + tan(A)*tan(B))",
        ["Both tangent values are defined.", "Denominator is not zero."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI036", "Double Angle Sine Identity", "identity",
        "Sine of twice an angle equals twice sine multiplied by cosine.",
        "sin(2*theta) = 2*sin(theta)*cos(theta)",
        ["Theta is a real angle."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI037", "Double Angle Cosine Identity", "identity",
        "Cosine of twice an angle has three equivalent forms.",
        "cos(2*theta) = cos(theta)^2 - sin(theta)^2 = 1 - 2*sin(theta)^2 = 2*cos(theta)^2 - 1",
        ["Theta is a real angle."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI038", "Double Angle Tangent Identity", "identity",
        "Tangent of twice an angle can be expressed using tangent of the angle.",
        "tan(2*theta) = 2*tan(theta) / (1 - tan(theta)^2)",
        ["tan(theta) is defined.", "1 - tan(theta)^2 is not zero."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI039", "Half Angle Sine Identity", "identity",
        "The square of sine of half an angle is related to cosine of the full angle.",
        "sin(theta/2)^2 = (1 - cos(theta)) / 2",
        ["Theta is a real angle."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI040", "Half Angle Cosine Identity", "identity",
        "The square of cosine of half an angle is related to cosine of the full angle.",
        "cos(theta/2)^2 = (1 + cos(theta)) / 2",
        ["Theta is a real angle."],
        domain="Trigonometry"
    ),

    # ---------------------------------------------------------
    # D. EXACT VALUES AND FUNCTION RESTRICTIONS
    # ---------------------------------------------------------

    create_assertion(
        "TRI041", "Sine of Common Angles", "property",
        "Sine has standard exact values at common angles.",
        "sin(0)=0; sin(pi/6)=1/2; sin(pi/4)=sqrt(2)/2; sin(pi/3)=sqrt(3)/2; sin(pi/2)=1",
        ["Angles are measured in radians."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI042", "Cosine of Common Angles", "property",
        "Cosine has standard exact values at common angles.",
        "cos(0)=1; cos(pi/6)=sqrt(3)/2; cos(pi/4)=sqrt(2)/2; cos(pi/3)=1/2; cos(pi/2)=0",
        ["Angles are measured in radians."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI043", "Tangent of Common Angles", "property",
        "Tangent has standard exact values at common angles.",
        "tan(0)=0; tan(pi/6)=sqrt(3)/3; tan(pi/4)=1; tan(pi/3)=sqrt(3)",
        ["Angles are measured in radians."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI044", "Undefined Tangent Values", "restriction",
        "Tangent is undefined where cosine equals zero.",
        "tan(theta) is undefined when theta = pi/2 + k*pi",
        ["k is an integer."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI045", "Undefined Cotangent Values", "restriction",
        "Cotangent is undefined where sine equals zero.",
        "cot(theta) is undefined when theta = k*pi",
        ["k is an integer."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI046", "Sine Range", "property",
        "The output of sine for real inputs lies between negative one and one.",
        "-1 <= sin(theta) <= 1",
        ["Theta is real."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI047", "Cosine Range", "property",
        "The output of cosine for real inputs lies between negative one and one.",
        "-1 <= cos(theta) <= 1",
        ["Theta is real."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI048", "Tangent Range", "property",
        "Tangent can take any real value where it is defined.",
        "Range of tan(theta) is all real numbers.",
        ["Theta excludes pi/2 + k*pi."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI049", "Inverse Sine Domain and Range", "property",
        "Inverse sine accepts inputs from negative one to one and returns principal angles.",
        "Domain = [-1,1]; Range = [-pi/2, pi/2]",
        ["Input lies between negative one and one."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI050", "Inverse Cosine Domain and Range", "property",
        "Inverse cosine accepts inputs from negative one to one and returns principal angles.",
        "Domain = [-1,1]; Range = [0,pi]",
        ["Input lies between negative one and one."],
        domain="Trigonometry"
    ),

    # ---------------------------------------------------------
    # E. INVERSE FUNCTIONS AND TRIGONOMETRIC EQUATIONS
    # ---------------------------------------------------------

    create_assertion(
        "TRI051", "Inverse Tangent Domain and Range", "property",
        "Inverse tangent accepts all real inputs and returns principal angles.",
        "Domain = all real numbers; Range = (-pi/2, pi/2)",
        ["Input is real."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI052", "Inverse Sine Evaluation", "concept",
        "Inverse sine returns the principal angle whose sine equals the given input.",
        "theta = arcsin(x)",
        ["-1 <= x <= 1."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI053", "Inverse Cosine Evaluation", "concept",
        "Inverse cosine returns the principal angle whose cosine equals the given input.",
        "theta = arccos(x)",
        ["-1 <= x <= 1."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI054", "Inverse Tangent Evaluation", "concept",
        "Inverse tangent returns the principal angle whose tangent equals the given input.",
        "theta = arctan(x)",
        ["x is real."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI055", "Basic Sine Equation", "method",
        "The equation sin(theta) = 0 has solutions at integer multiples of pi.",
        "theta = k*pi",
        ["k is an integer."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI056", "Basic Cosine Equation", "method",
        "The equation cos(theta) = 0 has solutions at odd multiples of pi/2.",
        "theta = pi/2 + k*pi",
        ["k is an integer."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI057", "Basic Tangent Equation", "method",
        "The equation tan(theta) = 0 has solutions at integer multiples of pi.",
        "theta = k*pi",
        ["k is an integer."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI058", "General Sine Equation", "method",
        "The equation sin(theta) = a has two families of solutions when -1 < a < 1.",
        "theta = arcsin(a) + 2*k*pi OR theta = pi - arcsin(a) + 2*k*pi",
        ["-1 <= a <= 1.", "k is an integer."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI059", "General Cosine Equation", "method",
        "The equation cos(theta) = a has two equivalent angle directions per full rotation when -1 < a < 1.",
        "theta = plus_or_minus arccos(a) + 2*k*pi",
        ["-1 <= a <= 1.", "k is an integer."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI060", "General Tangent Equation", "method",
        "The equation tan(theta) = a has solutions separated by pi radians.",
        "theta = arctan(a) + k*pi",
        ["a is real.", "k is an integer."],
        domain="Trigonometry"
    ),

    # ---------------------------------------------------------
    # F. TRIANGLE SOLVING RULES
    # ---------------------------------------------------------

    create_assertion(
        "TRI061", "Sine Rule", "formula",
        "The sine rule relates the sides of a triangle to the sines of their opposite angles.",
        "a/sin(A) = b/sin(B) = c/sin(C)",
        ["A, B, and C are angles of a triangle.", "Corresponding sides are opposite their angles."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI062", "Cosine Rule for Side", "formula",
        "The cosine rule calculates a side when two other sides and their included angle are known.",
        "c^2 = a^2 + b^2 - 2*a*b*cos(C)",
        ["a and b are known sides.", "C is the included angle."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI063", "Cosine Rule for Angle", "formula",
        "The cosine rule can calculate an angle from three known sides.",
        "cos(C) = (a^2 + b^2 - c^2) / (2*a*b)",
        ["a and b are positive.", "All three sides form a valid triangle."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI064", "Triangle Angle Sum", "property",
        "The interior angles of a Euclidean triangle add up to 180 degrees.",
        "A + B + C = pi radians",
        ["Triangle lies in Euclidean geometry."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI065", "Right Triangle Trigonometry", "method",
        "Right triangle trigonometry can determine unknown sides or angles using sine, cosine, and tangent.",
        "Use SOH-CAH-TOA to select the appropriate ratio.",
        ["Triangle contains one right angle.", "Required side or angle information is available."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI066", "Area of Triangle Using Sine", "formula",
        "The area of a triangle can be calculated using two sides and their included angle.",
        "Area = (1/2)*a*b*sin(C)",
        ["a and b are known sides.", "C is their included angle."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI067", "Ambiguous Sine Rule Case", "restriction",
        "The side-angle-side information is not required for the ambiguous case; SSA information may produce zero, one, or two valid triangles.",
        "Check all possible angles and triangle angle sums when using SSA.",
        ["Two sides and a non-included angle are given.", "Every candidate triangle must satisfy the angle sum and side constraints."],
        domain="Trigonometry"
    ),

    # ---------------------------------------------------------
    # G. TRIGONOMETRIC GRAPHS
    # ---------------------------------------------------------

    create_assertion(
        "TRI068", "Sine Graph Amplitude", "property",
        "The amplitude of a sine graph is the absolute value of its vertical coefficient.",
        "Amplitude = abs(A) for y = A*sin(B*x + C) + D",
        ["A is a real coefficient."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI069", "Cosine Graph Amplitude", "property",
        "The amplitude of a cosine graph is the absolute value of its vertical coefficient.",
        "Amplitude = abs(A) for y = A*cos(B*x + C) + D",
        ["A is a real coefficient."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI070", "Sine and Cosine Period", "formula",
        "The period of a sine or cosine graph depends on the absolute value of its horizontal coefficient.",
        "Period = 2*pi / abs(B)",
        ["B is not zero.", "Angles are measured in radians."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI071", "Tangent Graph Period", "formula",
        "The period of a tangent graph depends on the absolute value of its horizontal coefficient.",
        "Period = pi / abs(B)",
        ["B is not zero.", "Angles are measured in radians."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI072", "Vertical Shift of Trigonometric Graph", "property",
        "The constant D shifts a sine or cosine graph vertically.",
        "Midline: y = D",
        ["Function is in the form A*sin(B*x+C)+D or A*cos(B*x+C)+D."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI073", "Phase Shift of Trigonometric Graph", "property",
        "The horizontal phase shift depends on the ratio of the phase coefficient and horizontal coefficient.",
        "Phase shift = -C/B",
        ["B is not zero.", "Function is in the form A*sin(B*x+C)+D or A*cos(B*x+C)+D."],
        domain="Trigonometry"
    ),

    # ---------------------------------------------------------
    # H. VALIDITY AND VERIFICATION
    # ---------------------------------------------------------

    create_assertion(
        "TRI074", "Trigonometric Identity Verification", "verification",
        "A proposed trigonometric identity must hold for every input where both sides are defined.",
        "Simplify the difference between the two sides and verify that it equals zero on the common domain.",
        ["Both sides are mathematically defined.", "Domain restrictions are respected."],
        domain="Trigonometry"
    ),

    create_assertion(
        "TRI075", "Trigonometric Solution Verification", "verification",
        "Every proposed solution of a trigonometric equation must be substituted into the original equation.",
        "Verify each candidate solution in the original equation and reject candidates outside the requested interval.",
        ["Original equation is available.", "The requested interval and domain restrictions are respected."],
        domain="Trigonometry"
    ),

]



# ---------------------------------------------------------
# COMBINE ALL MATHEMATICAL ASSERTIONS
# ---------------------------------------------------------

ASSERTIONS = (
    ALGEBRA_ASSERTIONS
    + CALCULUS_ASSERTIONS
    + GEOMETRY_ASSERTIONS
    + TRIGONOMETRY_ASSERTIONS
)


