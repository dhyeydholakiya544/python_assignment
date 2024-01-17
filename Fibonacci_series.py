
def fibonacci_series(start, end):
    fibonacci_list = []
    a, b = 0, 1

    while a <= end:
        if a >= start:
            fibonacci_list.append(a)
        a, b = b, a + b

    return fibonacci_list


try:
   
    start_range = int(input("Enter the starting range: "))
    end_range = int(input("Enter the ending range: "))
    
  
    if start_range < 0 or end_range < 0 or start_range > end_range:
        print("Invalid range. Please enter a valid range.")
    else:
        
        result = fibonacci_series(start_range, end_range)
        print(f"The Fibonacci series in the range {start_range} to {end_range} is: {result}")
except ValueError:
    print("Invalid input. Please enter valid integers.")
