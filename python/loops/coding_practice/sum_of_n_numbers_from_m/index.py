m = int(input())
n = int(input())

count = 0
total = 0
current = m

while count < n:
    total = total + current
    current = current + 1
    count = count + 1

print(total)