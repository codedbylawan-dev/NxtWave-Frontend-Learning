word = input()

word_length = len(word)

first_character = word[0]

number_of_stars = word_length - 1

result = first_character + ("*" * number_of_stars)

print(result)