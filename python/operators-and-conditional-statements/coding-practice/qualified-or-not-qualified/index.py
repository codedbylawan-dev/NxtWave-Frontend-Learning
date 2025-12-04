maths = int(input())
physics = int(input())

is_both_greater = (maths > 35) and (physics > 35)

sum_of_marks = maths + physics
is_sum_greater = (sum_of_marks >= 100)

if is_both_greater or is_sum_greater:
    print("Qualified")
else:
    print("Not Qualified")
    