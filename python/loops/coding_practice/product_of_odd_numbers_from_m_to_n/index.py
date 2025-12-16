m = int(input())
n = int(input())

product = 1

for i in range(m, n + 1):
    if i % 2 == 1:
        product = product * i 

print(product)