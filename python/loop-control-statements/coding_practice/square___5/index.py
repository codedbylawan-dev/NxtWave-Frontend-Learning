s = int(input())
n = int(input())

row = ""

for i in range(n):
    row = row + str(s + i) + " "

for i in range(n):
    print(row)