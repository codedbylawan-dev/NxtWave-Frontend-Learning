m = int(input())
n = int(input())

found = False

for i in range(m, n + 1):
    if i % 6 == 0:
        print(i, end=" ")
        found = True 

if not found:
    print("No Numbers Found")