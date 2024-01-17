def get_first_and_last_chars(input_str):
    if len(input_str) < 2:
        return "Empty String"

    result_str = input_str[:2] + input_str[-2:]
    return result_str

user_input = input("Enter a string: ")
result = get_first_and_last_chars(user_input)
print("Result:", result)
