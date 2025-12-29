s = input()

vowels = "AEIOUaeiou"
result = ""

for ch in s:
    if ch not in vowels:
        result = result + ch 

print(result)