n = int(input())

top = "+ " + "- " * n + "+"
middle = "| " + "  " * n + "|"

print(top)

for i in range(n):
    print(middle)

print(top)