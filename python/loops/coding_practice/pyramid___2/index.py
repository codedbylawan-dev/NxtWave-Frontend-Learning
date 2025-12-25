n = int(input())

for row in range(1, n + 1):
    print("  " * (n - row) + (str(row) + " ") * (2 * row - 1))