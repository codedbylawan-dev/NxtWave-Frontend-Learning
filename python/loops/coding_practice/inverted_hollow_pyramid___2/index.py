n = int(input())

total_rows = 2 * n - 1

for i in range(total_rows):
    if i < n:
        num = i + 1
        left_spaces = "  " * (n - i - 1)
    else:
        num = total_rows - i
        left_spaces = "  " * (i - n + 1)
    
    if num == 1:
        print(left_spaces + str(num))
    else:
        inner_spaces = "  " * (num - 2)
        print(left_spaces + (str(num) + " ") + inner_spaces + str(num))