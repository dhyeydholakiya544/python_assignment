def reverse_string_if_multiple_of_4(input_str):
    if len(input_str) % 4 == 0:
        reversed_str = input_str[::-1]
        return reversed_str
    else:
        return input_str

input_string = "abcdefgh"
result = reverse_string_if_multiple_of_4(input_string)
print(result)
