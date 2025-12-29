s = input()

result = ""

for i in range(len(s)):
    if s[i].isupper() and i != 0:
        result = result + " "
    result = result + s[i]

print(result)