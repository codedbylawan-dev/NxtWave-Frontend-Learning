s = input()

result = ""

for ch in s:
    if ch.isupper():
        result = result + ch.lower()
    elif ch.islower():
        result = result = result + ch.upper()
    else:
        result = result + ch 
print(result)