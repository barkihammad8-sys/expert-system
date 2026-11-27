
# ============================================================
# MATHEMATICS EXPERT SYSTEM
# GEOMETRY SOLVER
# ============================================================

import sympy as sp


class GeometrySolver:

    def circle_area(self, radius):
        try:
            r = sp.sympify(radius)

            if r.is_positive is not True:
                raise ValueError("Radius must be positive.")

            result = sp.pi * r**2

            return {
                "status": "success",
                "operation": "Circle Area",
                "result": str(result),
                "approximate_result": str(sp.N(result))
            }

        except Exception:
            return {
                "status": "error",
                "message": "Invalid radius. Enter a positive number."
            }

    def circle_circumference(self, radius):
        try:
            r = sp.sympify(radius)

            if r.is_positive is not True:
                raise ValueError("Radius must be positive.")

            result = 2 * sp.pi * r

            return {
                "status": "success",
                "operation": "Circle Circumference",
                "result": str(result),
                "approximate_result": str(sp.N(result))
            }

        except Exception:
            return {
                "status": "error",
                "message": "Invalid radius. Enter a positive number."
            }

    def rectangle_area(self, length, width):
        try:
            l = sp.sympify(length)
            w = sp.sympify(width)

            if l.is_positive is not True or w.is_positive is not True:
                raise ValueError("Dimensions must be positive.")

            result = l * w

            return {
                "status": "success",
                "operation": "Rectangle Area",
                "result": str(result)
            }

        except Exception:
            return {
                "status": "error",
                "message": "Invalid rectangle dimensions."
            }

    def rectangle_perimeter(self, length, width):
        try:
            l = sp.sympify(length)
            w = sp.sympify(width)

            if l.is_positive is not True or w.is_positive is not True:
                raise ValueError("Dimensions must be positive.")

            result = 2 * (l + w)

            return {
                "status": "success",
                "operation": "Rectangle Perimeter",
                "result": str(result)
            }

        except Exception:
            return {
                "status": "error",
                "message": "Invalid rectangle dimensions."
            }

    def triangle_area(self, base, height):
        try:
            b = sp.sympify(base)
            h = sp.sympify(height)

            if b.is_positive is not True or h.is_positive is not True:
                raise ValueError("Dimensions must be positive.")

            result = sp.Rational(1, 2) * b * h

            return {
                "status": "success",
                "operation": "Triangle Area",
                "result": str(result)
            }

        except Exception:
            return {
                "status": "error",
                "message": "Invalid triangle dimensions."
            }

    def distance_between_points(self, x1, y1, x2, y2):
        try:
            x1, y1, x2, y2 = map(
                sp.sympify, [x1, y1, x2, y2]
            )

            result = sp.sqrt(
                (x2 - x1)**2 + (y2 - y1)**2
            )

            return {
                "status": "success",
                "operation": "Distance Between Points",
                "result": str(result)
            }

        except Exception:
            return {
                "status": "error",
                "message": "Invalid coordinates."
            }

    def midpoint(self, x1, y1, x2, y2):
        try:
            x1, y1, x2, y2 = map(
                sp.sympify, [x1, y1, x2, y2]
            )

            result = (
                (x1 + x2) / 2,
                (y1 + y2) / 2
            )

            return {
                "status": "success",
                "operation": "Midpoint",
                "result": str(result)
            }

        except Exception:
            return {
                "status": "error",
                "message": "Invalid coordinates."
            }

    def slope(self, x1, y1, x2, y2):
        try:
            x1, y1, x2, y2 = map(
                sp.sympify, [x1, y1, x2, y2]
            )

            if sp.simplify(x2 - x1) == 0:
                return {
                    "status": "undefined",
                    "message": "The line is vertical; its slope is undefined."
                }

            result = sp.simplify(
                (y2 - y1) / (x2 - x1)
            )

            return {
                "status": "success",
                "operation": "Slope",
                "result": str(result)
            }

        except Exception:
            return {
                "status": "error",
                "message": "Invalid coordinates."
            }


# Create default geometry solver
geometry_solver = GeometrySolver()
