word = input()

word_length = len(word)

first_letter = word[0]
last_letter = word[word_length - 1]

result = first_letter != last_letter

print(result)