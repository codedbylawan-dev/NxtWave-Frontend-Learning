word = input()

length = len(word)

for i in range(length):
    if i == length - 1:
        print(word[i])
    else:
        print(word[i], end="-")