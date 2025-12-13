s = input()

number = int(s[:-1])
last = s[-1]

if last == "T":
    print(number * 10)
elif last == "H":
    print(number * 100)
else:
    print(number * 1000)
    