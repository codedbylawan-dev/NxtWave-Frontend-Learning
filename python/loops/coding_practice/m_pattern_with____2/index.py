n = int(input())

for row in range(1, n + 1):
    leading = " " * (n - row)
    stars = "* " * row 
    middle = " " * (2 * (n - row))
    print(leading + stars + middle + stars)