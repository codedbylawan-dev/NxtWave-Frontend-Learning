s = input()

has_digit = False 

for ch in s:
    if ch.isdigit():
        has_digit = True 

if has_digit:
    print("Valid Password")
else:
    print("Invalid Password")