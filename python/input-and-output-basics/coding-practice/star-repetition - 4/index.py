word = input()

word_length = len(word)
number_of_stars = word_length - 4

first_two = word[:2]
last_two = word[-2:]

result = first_two + ("*" * number_of_stars) + last_two
print(result)