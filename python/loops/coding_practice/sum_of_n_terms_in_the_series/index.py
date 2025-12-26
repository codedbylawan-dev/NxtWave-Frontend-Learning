x = int(input())
n = int(input())


total = 0

for i in range(1, n + 1):
    power = 2 * i - 1
    value = x ** power

    if i % 2 == 0:
        value = -value 
    
    total = total + value

print(total)