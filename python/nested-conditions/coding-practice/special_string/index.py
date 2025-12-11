s = input()

prefix = s[0:3]
remaining = int(s[3:])

cond1 = (prefix == "NXT")
cond2 = (remaining % 2 == 0 or remaining % 7 == 0)

if cond1 and cond2:
    print("Special String")
else:
    print("Not a Special String")
    