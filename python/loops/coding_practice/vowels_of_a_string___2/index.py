word = input()

count = 0

for ch in word:
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        count = count + 1

if count > 2:
    print("String has more than two vowels")
else:
    print("String doesn't have more than two vowels")