n = int(input())

total_rows = 2 * n 

for i in range(total_rows):
    if i < n:
        stars = i + 1 
    else:
        stars = total_rows - i 
    
    middle_spaces = "  " * (2 * (n - stars))
    
    if stars == 1:
        print("* " + middle_spaces + "*")
    else:
        inner_spaces = "  " * (stars - 2)
        print("* " + inner_spaces + "* " + middle_spaces + "* " + inner_spaces + "*")