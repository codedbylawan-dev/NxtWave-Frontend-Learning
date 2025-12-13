d = input()
n = int(input())

if d == "Monday":
    start = 1
elif d == "Tuesday":
    start = 2
elif d == "Wednesday":
    start = 3
elif d == "Thursday":
    start = 4
elif d == "Friday":
    start = 5
elif d == "Saturday":
    start = 6
else:
    start = 7

final = (start + (n - 1)) % 7

if final == 0:
    final = 7

if final == 1:
    print("Monday")
elif final == 2:
    print("Tuesday")
elif final == 3:
    print("Wednesday")
elif final == 4:
    print("Thursday")
elif final == 5:
    print("Friday")
elif final == 6:
    print("Saturday")
else:
    print("Sunday")