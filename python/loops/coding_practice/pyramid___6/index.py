n = int(input())

for row in range(1, n + 1):
    spaces = " " * (n - row)
    stars = "* " * row 
    print(spaces + stars)