n = int(input())

for row in range(n, 0, -1):
    spaces = " " * (n - row)
    numbers = str(row) * row
    print(spaces + numbers)