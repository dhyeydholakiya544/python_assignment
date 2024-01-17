def swap_without_temp(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result_without_temp = swap_without_temp(num1, num2)
print(f"Swapped values (without temp variable): {result_without_temp}")
