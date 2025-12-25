n = int(input())

for row in range(1, n + 1):
    spaces = " " * (n - row)

    if row == n:
        print(spaces + "#" * n)
    else:
        print(spaces + "*" * row)