word = input()

n = len(word)

for i in range(n, 0, -1):
    print(word[:i])