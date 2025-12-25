n = int(input())

total_rows = 2 * n - 1

for row in range(1, total_rows + 1):
    if row <= n:
        spaces = "  " * (n - row)
        plus = "+ " * (row - 1) + "#"
    else:
        spaces = "  " * (row - n)
        plus = "+ " * (total_rows - row) + "#"
    
    print(spaces + plus)