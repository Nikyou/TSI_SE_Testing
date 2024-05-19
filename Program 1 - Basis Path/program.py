def triangle_type(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid Input: Side lengths must be positive."
    if a + b <= c or b + c <= a or a + c <= b:
        return "Invalid Input: The sum of any two sides must be greater than the third side."
    if a == b == c:
        return "Triangle type: Equilateral"
    if a == b or b == c or a == c:
        return "Triangle type: Isosceles"
    return "Triangle type: Scalene"

sides_input = input("Enter the length of sides (separated by spaces): ").split()
if len(sides_input) != 3:
    print("\n")
    print("Invalid Input: Please enter exactly 3 numbers.")
    exit(1)

try:
    a, b, c = map(float, sides_input)
except ValueError:
    print("\n")
    print("Invalid Input: Please enter valid numerical values for side lengths.")
    exit(1)

triangle = triangle_type(a, b, c)
print("\n")
print(triangle)