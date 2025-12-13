n = int(input())

a = n // 1000
n = n - a * 1000

b = n // 500
n = n - b * 500

c = n // 100
n = n - c * 100

d = n // 50
n = n - d * 50

e = n // 20
n = n - e * 20

f = n // 5
n = n - f * 5

g = n // 1
n = n - g * 1

print("1000:" + str(a))
print("500:" + str(b))
print("100:" + str(c))
print("50:" + str(d))
print("20:" + str(e))
print("5:" + str(f))
print("1:" + str(g))