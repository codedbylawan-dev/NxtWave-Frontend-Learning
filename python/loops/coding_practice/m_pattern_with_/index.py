n = int(input())

for i in range(1, n + 1):
    spaces = "  " * (n - i)
    row = ("* " * i) + spaces + spaces + ("* " * i)
    print(row)