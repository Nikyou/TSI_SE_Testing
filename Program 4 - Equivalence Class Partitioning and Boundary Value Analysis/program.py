n = input("Enter a non-negative integer: ").split()
print("\n")

try:
    n = list(map(int, n))
except ValueError:
    print("Invalid Input: not an integer")
    exit(1)

if len(n) != 1:
    print("Invalid Input: incorrect number of inputs")
    exit(1)

n = n[0]

if n < 0:
    print("Invalid Input: integer must be non-negative")
    exit(1)

result = 1
if n != 0:
    for i in range(1, n + 1):
        result *= i

print("The factorial is", result)