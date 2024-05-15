def triangle_type(a, b, c):                                                                     #7
    if a <= 0 or b <= 0 or c <= 0:                                                              #8
        return "Invalid Input: Side lengths must be positive."                                  #9
    elif a + b <= c or b + c <= a or a + c <= b:                                                #10
        return "Invalid Input: The sum of any two sides must be greater than the third side."   #11
    elif a == b == c:                                                                           #12
        return "Triangle type: Equilateral"                                                     #13
    elif a == b or b == c or a == c:                                                            #14
        return "Triangle type: Isosceles"                                                       #15
    else:                                                                                       #16
        return "Triangle type: Scalene"                                                         #16

sides_input = input("Enter the length of sides (separated by spaces): ").split()                #1
if len(sides_input) != 3:                                                                       #2
    print("\n")                                                                                 #3
    print("Invalid Input: Please enter exactly 3 numbers.")                                     #3
    exit(1)                                                                                     #3

try:                                                                                            #4
    a, b, c = map(float, sides_input)                                                           #5
except ValueError:                                                                              #6
    print("\n")                                                                                 #6
    print("Invalid Input: Please enter valid numerical values for side lengths.")               #6
    exit(1)                                                                                     #6

triangle = triangle_type(a, b, c)                                                               #7
print("\n")                                                                                     #17
print(triangle)                                                                                 #17