n = int(input())

total_digits = 0

for number in range(1, n + 1):
    total_digits = total_digits + len(str(number))

print(total_digits)