m = int(input())
n = int(input())

total = 0

for i in range(m, n + 1):
    total = total + (i * i)

print(total)