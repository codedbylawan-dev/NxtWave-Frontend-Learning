s = input()

result = ""

for ch in s:
    if ch.isupper():
        result = result + ch

print(result)