n = int(input())

for row in range(n, 0, -1):
    spaces = " " * (n - row)
    stars = "*" * (2 * row - 1)
    print(spaces + stars)
    