first_angle = int(input())
second_angle = int(input())
third_angle = int(input())

sum_of_three_angles = first_angle + second_angle + third_angle

if sum_of_three_angles == 180:
    print("It's a Triangle")
else:
    print("It's not a Triangle")