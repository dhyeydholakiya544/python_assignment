def sum_of_positive_integers(n):
    if n < 0:
        return "Invalid input. Please enter a non-negative integer."
    else:
        return (n * (n + 1)) // 2

try:
    n = int(input("Enter a non-negative integer (n): "))
    result = sum_of_positive_integers(n)
    print(f"The sum of the first {n} positive integers is: {result}")
except ValueError:
    print("Invalid input. Please enter a valid non-negative integer.")
