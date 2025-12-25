x = int(input())
n = int(input())

total = 0
power = 2
sign = 1

for i in range(n):
    total = total + (sign * (x ** power))
    power = power + 2
    sign = sign * -1

print(total)