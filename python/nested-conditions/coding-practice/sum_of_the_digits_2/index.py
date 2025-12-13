s = input()
l = len(s)

if l == 1:
    total = int(s[0])
elif l == 2:
    total = int(s[0]) + int(s[1])
elif l == 3:
    total = int(s[0]) + int(s[1]) + int(s[2])
elif l == 4:
    total = int(s[0]) + int(s[1]) + int(s[2]) + int(s[3])
else:
    total = int(s[0]) + int(s[1]) + int(s[2]) + int(s[3]) + int(s[4])

print(total)