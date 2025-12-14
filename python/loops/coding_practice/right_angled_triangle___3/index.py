n = int(input())

row = 1
while row <= n:
    if row < n:
        print(("* ") * row)
    else:
        print("+ " * n)
    row = row + 1