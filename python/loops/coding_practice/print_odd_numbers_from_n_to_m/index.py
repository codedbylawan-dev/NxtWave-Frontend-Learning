m = int(input())
n = int(input())

result = ""
for i in range(n, m - 1, -1):
    if i % 2 != 0:
        result = result + str(i) + " "

print(result)
