a = int(input())

hund = a // 100
remaining = a - hund * 100

fifty = remaining // 50
remaining = remaining - fifty * 50

twenty = remaining // 20
remaining = remaining - twenty * 20

ten = remaining // 10

print("100 Notes: " + str(hund))
print("50 Notes: " + str(fifty))
print("20 Notes: " + str(twenty))
print("10 Notes: " + str(ten))
