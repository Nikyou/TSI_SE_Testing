def find_max(numbers):
    if not numbers:
        return None

    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num

    return max_value

numbers = input("Enter numbers to find maximum (separated by spaces): ").split()
print("\n")

try:
    numbers = list(map(float, numbers))
except ValueError:
    print("Invalid Input")
    exit(1)

result = find_max(numbers)
if result:
    print("The maximum value is:", result)
else:
    print("Invalid Input")