n = int(input())

k = n * (n + 1) // 2

num = k 
space = 0

for i in range(n, 0, -1):
    print(" " * space, end="")
    for j in range(i):
        print(num, end=" ")
        num = num - 1
    print()
    space = space + 2