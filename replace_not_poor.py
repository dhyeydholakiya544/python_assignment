def replace_not_poor(s):
    index_not = s.find('not')
    index_poor = s.find('poor')

    if index_not != -1 and index_poor != -1 and index_not < index_poor:
        s = s[:index_not] + 'good' + s[index_poor + 4:]

    return s

input_string = "The weather is not poor today. I hope it gets better, not worse."
result = replace_not_poor(input_string)
print(result)
