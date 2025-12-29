s = input()

has_upper = False
has_lower = False
has_digit = False

for ch in s:
    if ch.isupper():
        has_upper = True
    if ch.islower():
        has_lower = True
    if ch.isdigit():
        has_digit = True 

if has_upper and has_lower and has_digit:
    print("Valid Password")
else:
    print("Invalid Password")