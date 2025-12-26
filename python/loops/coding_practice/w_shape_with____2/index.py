n = int(input())

for row in range(1, n + 1):
    left_spaces = " " * (row - 1)
    left_stars = "* " * (n - row + 1)
    middle_spaces = "  " * (row - 1)
    right_stars = "* " * (n - row + 1)

    print(left_spaces + left_stars + middle_spaces + right_stars)