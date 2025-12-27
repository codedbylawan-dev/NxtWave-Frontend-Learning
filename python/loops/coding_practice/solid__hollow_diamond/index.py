n = int(input())

total_rows = 2 * n - 1

for i in range(total_rows):

    if i < n:
        # Solid Pyramid (Top)
        left_spaces = " " * (n - i - 1)
        stars = "* " * (i + 1)
        print(left_spaces + stars)

    else:
        # Hollow Inverted Pyramid (Bottom)
        row = i - n + 1
        left_spaces = " " * row

        if row == n - 1:
            print(left_spaces + "*")
        else:
            inner_spaces = " " * (2 * (n - row - 1) - 2)
            print(left_spaces + "* " + inner_spaces + "*")