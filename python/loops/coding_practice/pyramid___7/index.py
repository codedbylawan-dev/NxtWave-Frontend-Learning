n = int(input())

for row in range(1, n + 1):
    spaces = " " * (n - row)
    numbers = (str(row) + " ") * row
    print(spaces + numbers)