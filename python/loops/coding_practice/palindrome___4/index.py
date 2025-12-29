s = input()

s = s.lower()
s = s.replace(" ", "")
s = s.replace("'", "")

rev = s[::-1]

if s == rev:
    print(True)
else:
    print(False)