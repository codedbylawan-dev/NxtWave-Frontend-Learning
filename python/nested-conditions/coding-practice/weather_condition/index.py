t = float(input())

if t < 0:
    print("Freezing weather")
elif t < 10:
    print("Very Cold weather")
elif t < 20:
    print("Cold weather")
elif t < 30:
    print("Normal")
elif t < 40:
    print("Hot")
else:
    print("Very Hot")
    