
from mathematics_solver.geometry import GeometrySolver

solver = GeometrySolver()

print("=" * 45)
print("GEOMETRY SOLVER TESTING")
print("=" * 45)

# TEST 1: Circle area
result = solver.circle_area(7)

assert result["status"] == "success"
assert result["result"] == "49*pi"

print("Test 1 - Circle area:          PASSED")
print("Result:", result["result"])


# TEST 2: Circle circumference
result = solver.circle_circumference(7)

assert result["result"] == "14*pi"

print("Test 2 - Circumference:        PASSED")


# TEST 3: Rectangle area
result = solver.rectangle_area(10, 5)

assert result["result"] == "50"

print("Test 3 - Rectangle area:       PASSED")


# TEST 4: Rectangle perimeter
result = solver.rectangle_perimeter(10, 5)

assert result["result"] == "30"

print("Test 4 - Rectangle perimeter:  PASSED")


# TEST 5: Triangle area
result = solver.triangle_area(10, 6)

assert result["result"] == "30"

print("Test 5 - Triangle area:        PASSED")


# TEST 6: Distance between points
result = solver.distance_between_points(0, 0, 3, 4)

assert result["result"] == "5"

print("Test 6 - Distance:             PASSED")


# TEST 7: Midpoint
result = solver.midpoint(2, 4, 6, 8)

assert result["result"] == "(4, 6)"

print("Test 7 - Midpoint:             PASSED")


# TEST 8: Vertical line slope
result = solver.slope(2, 1, 2, 5)

assert result["status"] == "undefined"

print("Test 8 - Vertical slope:       PASSED")


print("-" * 45)
print("ALL GEOMETRY SOLVER TESTS PASSED!")
print("=" * 45)
