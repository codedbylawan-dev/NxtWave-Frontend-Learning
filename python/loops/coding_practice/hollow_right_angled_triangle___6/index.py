n = int(input())

for i in range(n):
    left_spaces = "  " * i 

    if i == 0:
        print("* " * n)
    elif i == n - 1:
        print(left_spaces + "*")
    else:
        inner_spaces = "  " * (n - i - 2)
        print(left_spaces + "* " + inner_spaces + "*")