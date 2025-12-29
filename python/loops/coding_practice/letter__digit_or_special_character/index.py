c = input()

if 'a' <= c <= 'z':
    print("Lowercase Letter")
elif 'A' <= c <= 'Z':
    print("Uppercase Letter")
elif '0' <= c <= '9':
    print("Digit")
else:
    print("Special Character")