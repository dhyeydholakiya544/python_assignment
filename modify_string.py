def modify_string(input_str):
    if len(input_str) >= 3:
        if input_str.endswith('ing'):
            modified_str = input_str + 'ly'
        else:
            modified_str = input_str + 'ing'
    else:
        modified_str = input_str

    return modified_str

user_input = input("Enter a string: ")
result = modify_string(user_input)
print("Modified string:", result)
