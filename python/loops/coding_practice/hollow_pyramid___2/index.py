n = int(input())

total_rows = 2 * n - 1

for i in range(1, total_rows + 1):
    if i <= n:
        num = i 
    else:
        num = total_rows - i + 1
    
    if num == 1:
        print("1")
    else:
        inner_spaces = "  " * (num - 2)
        print(str(num) + " " + inner_spaces + str(num))