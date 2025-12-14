x = int(input())
n = int(input())

count = 0
product = 1
current = x + 1

while count < n:
    product = product * current
    current = current + 1
    count = count + 1

print(product)