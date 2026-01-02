s = int(input())
n = int(input())

for i in range(1, n + 1):
    for space in range(n - i):
        print(" ", end="")
    num = s 
    for j in range(i):
        print(num, end=" ")
        num = num + 1 
    print()