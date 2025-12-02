a = int(input())
s = input()

is_age_valid = (a > 12) and (a < 60)

is_guardian_yes = (5 == "yes")

result = is_age_valid or is_guardian_yes

print(result)