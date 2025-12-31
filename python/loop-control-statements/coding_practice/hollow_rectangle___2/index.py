m = int(input())
n = int(input())

rows = m + 2
cols = n + 2

for r in range(1, rows + 1):
    if r == 1 or r == rows:
        print("+" + "-" * (cols - 2) + "+")
    else:
        print("|" + " " * (cols - 2) + "|")