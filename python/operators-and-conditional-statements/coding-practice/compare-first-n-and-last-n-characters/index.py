s = input()
n = int(input())

first_n = s[:n]
last_n = s[-n:]

print(first_n != last_n)