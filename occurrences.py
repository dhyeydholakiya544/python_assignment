def count_word_occurrences(sentence):
    word_occurrences = {}
    words = sentence.split()
    for word in words:
        word = word.strip(".,!?()[]{}\"'")
        word = word.lower()
        word_occurrences[word] = word_occurrences.get(word, 0) + 1
    
    return word_occurrences
user_sentence = input("Enter a sentence: ")
result = count_word_occurrences(user_sentence)
print("Word occurrences in the sentence:")
for word, occurrences in result.items():
    print(f"{word}: {occurrences}")
