m = int(input())
n = int(input())

row_num = 1
count = 0

while count < m:
    row = (str(row_num) + " ") * n 
    print(row)
    row_num = row_num + 1
    count = count + 1
    