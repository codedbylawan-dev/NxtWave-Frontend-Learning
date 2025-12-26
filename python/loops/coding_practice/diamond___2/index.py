n = int(input())

for row in range(1, 2 * n):
    if row <= n:
        current = row
    else:
        current = 2 * n - row 
    
    spaces = " " * (n - current)
    numbers = (str(current) + " ") * current
    print(spaces + numbers)