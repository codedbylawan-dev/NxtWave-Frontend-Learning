s = input()

result = ""

for ch in s:
    if ch.isupper():
        result = result + "-" + ch.lower()
    else:
        result = result + ch 

print(result)