s = input()

has_upper = False

for ch in s:
    if ch.isupper():
        has_upper = True

if has_upper:
    print("Valid Password")
else:
    print("Invalid Password")