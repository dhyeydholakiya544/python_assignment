def is_vowel(letter):
    vowels = "aeiouAEIOU"
    return letter in vowels
try:
    char = input("Enter a letter: ")[0]
    
    if char.isalpha() and len(char) == 1:
        if is_vowel(char):
            print(f"The letter '{char}' is a vowel.")
        else:
            print(f"The letter '{char}' is not a vowel.")
    else:
        print("Invalid input. Please enter a single alphabet character.")
except IndexError:
    print("Invalid input. Please enter a single alphabet character.")
