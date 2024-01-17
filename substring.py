def count_substring_occurrences(main_string, substring):
    count = 0
    start_index = 0
    while start_index != -1:
        start_index = main_string.find(substring, start_index)
        if start_index != -1:
            count += 1
            start_index += 1
    
    return count
main_str = input("Enter the main string: ")
sub_str = input("Enter the substring to count: ")
result = count_substring_occurrences(main_str, sub_str)
print(f"The substring '{sub_str}' occurs {result} times in the main string.")
