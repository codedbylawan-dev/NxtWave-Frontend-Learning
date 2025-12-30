m = int(input())
n = int(input())

row_pattern = ""

for i in range(1, n + 1):
    row_pattern = row_pattern + str(i) + " "

for _ in range(m):
    print(row_pattern)