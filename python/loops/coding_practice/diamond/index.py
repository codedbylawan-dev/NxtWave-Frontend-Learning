n = int(input())

total_rows = 2 * n - 1

for row in range(1, total_rows + 1):
    if row <= n:
        spaces = " " * (n - row)
        stars = "* " * row 
    else:
        spaces = " " * (row - n)
        stars = "* " * (total_rows - row + 1)
    
    print(spaces + stars)