first_number = int(input())
second_number = int(input())

is_less_than = (first_number < 20) or (second_number < 20)

sum_of_numbers = first_number + second_number
is_sum_between = (sum_of_numbers > 30) and (sum_of_numbers < 50)

if is_less_than or is_sum_between:
    print(sum_of_numbers)
else:
    print(first_number)
    print(second_number)