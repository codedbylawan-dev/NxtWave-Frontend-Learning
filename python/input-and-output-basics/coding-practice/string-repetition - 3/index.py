word = input()
n = int(input())

length_of_the_word = len(word)
start_index = length_of_the_word - 3
sliced_word = word[start_index:]

message = sliced_word * n 

print(message)