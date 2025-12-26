n = int(input())

for i in range(1, 2 * n):
    if i <= n:
        current = i
    else:
        current = 2 * n - i
    
    spaces = " " * (n - current)

    if current == 1:
        print(spaces + "*")
    else:
        hollow_spaces = " " * (2 * current - 3)
        print(spaces + "*" + hollow_spaces + "*")