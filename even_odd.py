def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

try:
    num = int(input("Enter a number: "))
   
    result = check_even_odd(num)
    print(f"The number {num} is {result}.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
