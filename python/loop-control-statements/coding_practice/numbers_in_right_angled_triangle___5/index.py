s = int(input())
n = int(input())

k = n * (n + 1) // 2
num = k + s - 1

for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num = num - 1
    print()