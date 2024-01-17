def count_character_frequency(input_string):
    char_frequency = {}
    
    for char in input_string:
        char_frequency[char] = char_frequency.get(char, 0) + 1
    
    return char_frequency
user_input = input("Enter a string: ")
result = count_character_frequency(user_input)
print("Character frequency in the string:")
for char, frequency in result.items():
    print(f"{char}: {frequency}")
