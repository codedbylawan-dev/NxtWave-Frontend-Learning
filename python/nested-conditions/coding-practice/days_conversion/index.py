n = int(input())

years = n // 365
remaining = n % 365

week = remaining // 7
days = remaining % 7

print(years, "years", week, "weeks", days, "days")
