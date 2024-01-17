def sum_with_condition(a, b, c):
    if a == b or b == c or a == c:
        return 0
    else:
        return a + b + c
try:
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))
    num3 = int(input("Enter the third integer: "))
    
    result = sum_with_condition(num1, num2, num3)
    print(f"The sum is: {result}")
except ValueError:
    print("Invalid input. Please enter valid integers.")
