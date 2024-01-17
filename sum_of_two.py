def check_condition(a, b):
    return a == b or a + b == 5 or abs(a - b) == 5

try:
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))

    result = check_condition(num1, num2)
    print(f"The condition is {result}")
except ValueError:
    print("Invalid input. Please enter valid integers.")
