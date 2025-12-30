s = input()

result = ""

first = True

for ch in s:
    if "A" <= ch <= "Z":
        if not first:
            result = result + "-"
        result = result + (ch.lower())
        first = False
    else:
        result = result + ch

print(result)