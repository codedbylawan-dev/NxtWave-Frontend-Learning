word = input()

length_of_the_word = len(word)
half_length = length_of_the_word / 2 
half_length = int(half_length)

half_word = word[:half_length]

print(half_word)