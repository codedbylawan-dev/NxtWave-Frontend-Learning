n = int(input())

spaces = n - 1
stars = 1

for i in range(n):
    print(" " * spaces + "* " * stars)
    spaces = spaces - 1
    stars = stars + 1