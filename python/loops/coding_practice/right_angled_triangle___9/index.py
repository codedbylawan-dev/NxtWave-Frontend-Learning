n = int(input())

for row in range(1, n + 1):
    if row == 1:
        print(". ")
    elif row == n:
        print(". " * n)
    else:
        print(". " + "0 " * (row - 2) + ". ")