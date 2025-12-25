n = int(input())

total_rows = 2 * n - 1

for row in range(1, total_rows + 1):
    if row <= n:
        stars = row 
        spaces = 2 * (n - row)
    else:
        stars = total_rows - row + 1
        spaces = 2 * (row - n)
        
    print("* " * stars + "  " * spaces + "* " * stars)