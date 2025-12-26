n = int(input())

for i in range(1, n + 1):
    spaces = " " * (n - i)

    if i == 1:
        print(spaces + "*")
    elif i == n:
        print("* " * n)
    else:
        hollow_spaces = " " * (2 * i - 3)
        print(spaces + "*" + hollow_spaces + "*")