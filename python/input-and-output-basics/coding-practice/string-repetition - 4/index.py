word = input()
n = int(input())

new_string = word + (" " + word) * (n - 1)

print(new_string)