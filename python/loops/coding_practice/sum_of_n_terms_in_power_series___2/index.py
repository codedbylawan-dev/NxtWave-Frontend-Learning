x = int(input())
n = int(input())

total = 0
power = 2

for i in range(n):
    total = total + (x ** power)
    power = power + 2

print(total)