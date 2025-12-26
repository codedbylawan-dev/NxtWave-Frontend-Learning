n = int(input())

for row in range(0, n + 1):
    if row == 0:
        print("_" * (n + 1))
    else:
        print("|" + " " * (n - row) + "/")