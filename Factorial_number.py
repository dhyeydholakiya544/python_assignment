
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


try:
    num = int(input("Enter a number: "))
    
    if num < 0:
        print("Factorial is undefined for negative numbers.")
    else:
       
        result = factorial(num)
        print(f"The factorial of {num} is {result}.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
