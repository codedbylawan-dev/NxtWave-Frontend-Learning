size = input()
pages = int(input())

can_buy = (size == 'large') or (pages >= 300)

if can_buy:
    print("Buy a Book")
else:
    print("Do Not Buy a Book")
    