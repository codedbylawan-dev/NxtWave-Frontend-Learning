m = int(input())
n = int(input())

total_digits = 0

for i in range(m, n + 1):
    total_digits = total_digits + len(str(i))

print(total_digits)