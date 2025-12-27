n = int(input())

total = 0

for i in range(1, n + 1):
    term = int("1" * i)
    total = total + term

print(total)