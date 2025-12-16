m = int(input())
n = int(input())

result = ""

for i in range(m , n + 1):
    if i % 2 != 0:
        result = result + str(i) + " "

print(result)