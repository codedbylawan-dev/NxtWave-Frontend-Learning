s = input()

is_valid = True

for ch in s:
    if not ch.isdigit():
        is_valid = False

print(is_valid)