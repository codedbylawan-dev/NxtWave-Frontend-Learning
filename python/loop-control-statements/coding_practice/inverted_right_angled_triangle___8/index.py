n = int(input())

for row in range(n):
    spaces = "  " * (row * 2)
    stars = "* " * (2 * (n - row) - 1)
    print(spaces + stars)