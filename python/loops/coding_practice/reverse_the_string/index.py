s = input()

result = ""
length = len(s)

for i in range(length - 1, -1, -1):
    result = result + s[i]

print(result)