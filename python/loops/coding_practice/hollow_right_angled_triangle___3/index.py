n = int(input())

for i in range(n):
    if i == 0:
        print("* " * n)
    elif i == n - 1:
        print("* ")
    else:
        inner_spaces = "  " * (n - i - 2)
        print("* " + inner_spaces + "* ")