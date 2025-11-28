word = input()

length_of_word = len(word)

first_char = word[0]
last_char = word[length_of_word - 1]

middle_length = len(word) - 2 

middle_stars = "*" * middle_length

result = first_char + middle_stars + last_char

print(result)