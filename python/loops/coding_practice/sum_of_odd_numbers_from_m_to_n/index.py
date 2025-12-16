m = int(input())
n = int(input())

total = 0

for i in range(m , n + 1):
    if i % 2 == 1:
        total = total + i 

print(total)