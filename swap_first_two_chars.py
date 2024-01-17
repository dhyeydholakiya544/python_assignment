def swap_first_two_chars(s):
    return s[1] + s[0] + s[2:]

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if len(string1) >= 2 and len(string2) >= 2:
    swapped_string1 = swap_first_two_chars(string1)
    swapped_string2 = swap_first_two_chars(string2)

    result_string = swapped_string1 + ' ' + swapped_string2

    print("Result:", result_string)
else:
    print("Both strings should have at least two characters.")
