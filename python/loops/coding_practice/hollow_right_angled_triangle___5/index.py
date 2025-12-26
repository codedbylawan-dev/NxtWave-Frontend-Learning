n = int(input())

for row in range(1, n + 1):
    left_spaces = "  " * (n - row)

    if row == 1:
        print(left_spaces + "*")
    elif row == n:
        print("* " * n)
    else:
        inner_spaces = "  " * (row - 2)
        print(left_spaces + "* " + inner_spaces + "*")