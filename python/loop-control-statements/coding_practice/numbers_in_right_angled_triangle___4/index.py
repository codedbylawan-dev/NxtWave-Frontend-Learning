s = int(input())
n = int(input())

num = s 

for i in range(1, n + 1):
    for j in range(2 * i):
        print(num, end=" ")
        num = num + 1 
    print()