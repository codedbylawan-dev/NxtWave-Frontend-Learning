s1 = input()
s2 = input()

result = ''

for i in range(len(s1)):
    if i % 2 == 0:
        result = result + s1[i]
    else:
        result = result + s2[i]

print(result)

