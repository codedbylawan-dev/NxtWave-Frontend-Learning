n = int(input())

count = 1

while count <= n:
    line = (str(count) + " ") * count
    print(line)
    count = count + 1