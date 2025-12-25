n = int(input())

for row in range(1, 2 * n):
    if row <= n:
        print((str(row) + " ") * row)
    else:
        value = 2 * n - row
        print((str(value) + " ") * value)