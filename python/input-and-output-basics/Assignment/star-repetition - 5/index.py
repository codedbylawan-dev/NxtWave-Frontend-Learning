w1 = input()
w2 = input()

length_w2 = len(w2)

result = "*" * length_w2 + w1[length_w2:]

print(result)