m = int(input())
n = int(input())

for row in range(1, m + 1):
    if row % 2 != 0:
        print("+ " * n)
    else:
        print("_ " * n)
