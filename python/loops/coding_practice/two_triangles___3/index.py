# n = int(input())

# for i in range(n):
    
#     if i == 0:
#         spaces = "  " * (2 * n - 2)
#         print("* " + spaces + "* ")
#     elif i == n - 1:
#         print("* " * (2 * n))
#     else:
#         spaces = "  " * (2 * (n - i) - 2)
#         print("* " + ("  " * (i - 1)) + "* " + spaces + "* " + ("  " * (i - 1)) + "* ")

n = int(input())

for i in range(n):
    if i == 0:
        spaces = "  " * (2 * n - 2)
        print("* " + spaces + "*")
    
    elif i == n - 1:
        print("* " * (2 * n))
    
    else:
        left_hollow = "  " * (i - 1)
        middle_spaces = "  " * (2 * (n - i) - 2)

        print(
            "* " +
            left_hollow +
            "* " +
            middle_spaces +
            "* " +
            left_hollow +
            "*"
        )
