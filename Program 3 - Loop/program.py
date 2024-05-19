arr = input("Enter numbers to sort (separated by spaces): ").split()
print("\n")

try:
    arr = list(map(float, arr))
except ValueError:
    print("Invalid Input")
    exit(1)

n = len(arr)
for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

if n > 0:
    print("Sorted array:", ' '.join(map(str, arr)))
else:
    print("Invalid Input")