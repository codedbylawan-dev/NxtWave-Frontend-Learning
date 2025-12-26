n = int(input())

for row in range(1, n + 1):
    spaces = "  " * (row - 1)
    stars = "* " * (n - row + 1)
    print(spaces + stars)