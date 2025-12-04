first_number = int(input())
second_number = int(input())
third_number = int(input())

is_all_greater = (first_number > 100) and (second_number > 100) and (third_number > 100)

if is_all_greater:
    print("All are greater than 100")
else:
    print("Not all are greater than 100")
    