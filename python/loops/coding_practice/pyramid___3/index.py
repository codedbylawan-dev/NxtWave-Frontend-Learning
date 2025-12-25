n = int(input())

for row in range(1, 2 * n):
    if row <= n:
        print("* " * row)
    else:
        print("* " * (2 * n - row))