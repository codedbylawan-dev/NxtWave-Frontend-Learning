s = input()
n = len(s)

result = ""

for i in range(n):
    idx = int(input())
    result = result + s[idx]

print(result)