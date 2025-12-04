number = int(input())

n_str = str(number)
digit_1 = int(n_str[0])
digit_2 = int(n_str[1])
digit_3 = int(n_str[2])

is_any_digit_not_five = (digit_1 != 5) or (digit_2 != 5) or (digit_3 != 5)
is_between = (number > 300) and (number < 700)

if is_any_digit_not_five and is_between:
    print("Valid Number")
else:
    print("Not a Valid Number")