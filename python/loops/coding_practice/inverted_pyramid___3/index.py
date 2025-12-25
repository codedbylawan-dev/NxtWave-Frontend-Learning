n = int(input())

for i in range(n):
    spaces = " " * i 
    if i == 0:
        symbols = "+ " * n 
    else:
        symbols = "* " * (n - i)
    
    print(spaces + symbols)