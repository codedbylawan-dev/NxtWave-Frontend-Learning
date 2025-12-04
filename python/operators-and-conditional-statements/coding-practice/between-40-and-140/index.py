first_number = int(input())
second_number = int(input())

is_first_between = (first_number > 40) and (first_number < 140)
is_second_between = (second_number > 40) and (second_number < 140)

if is_first_between or is_second_between:
    print("Between 40 and 140: Yes")
else:
    print("Between 40 and 140: No")