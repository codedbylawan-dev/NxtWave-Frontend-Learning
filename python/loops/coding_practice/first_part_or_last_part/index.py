s1 = input()
s2 = input()

if s1[:len(s2)] == s2 or s1[-len(s2):] == s2:
    print(True)
else:
    print(False)