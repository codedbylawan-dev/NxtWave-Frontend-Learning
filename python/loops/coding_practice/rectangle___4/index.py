m = int(input())
n = int(input())

for row in range(1, m + 1):
    if row == 1 or row == m:
        print("* " * n)
    else:
        print("* " + "0 " * (n - 2) + "* ")