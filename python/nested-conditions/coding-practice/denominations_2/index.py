a = int(input())

hund = a // 100
a = a % 100

fifty = a // 50
a = a % 50

ten = a // 10
a = a % 10

one = a 

print("100:" + str(hund))
print("50:" + str(fifty))
print("10:" + str(ten))
print("1:" + str(one))