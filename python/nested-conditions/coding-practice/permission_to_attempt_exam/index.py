a = input()
m = input()

attendance = int(a[:1])

if attendance >= 75 or m == "Y":
    print("Allowed to write exam")
else:
    print("Cannot write exam")