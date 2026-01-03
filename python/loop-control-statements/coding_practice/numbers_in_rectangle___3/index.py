m = int(input())
n = int(input())

k = m * n 
num = k 

for i in range(m):
    for j in range(n):
        print(num, end=" ")
        num = num - 1 
    print()