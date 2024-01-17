def find_longest_word_length(word_list):
    if not word_list:
        return 0

    longest_length = 0

    for word in word_list:
        if len(word) > longest_length:
            longest_length = len(word)

    return longest_length

words = ["apple", "banana", "kiwi", "grapefruit"]
result = find_longest_word_length(words)
print(f"The length of the longest word is: {result}")
