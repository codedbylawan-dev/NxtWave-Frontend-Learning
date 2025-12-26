n = int(input())

for i in range(n):
    spaces = " " * i

    if i == 0:
        print("* " * n)
    elif i == n - 1:
        print(spaces + "*")
    else:
        inner_spaces = "  " * ((n - i) - 2)
        print(spaces + "* " + inner_spaces + "*")