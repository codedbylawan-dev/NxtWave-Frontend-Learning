abhinav = input()
anjali = input()

if abhinav == anjali:
    print("Tie")
elif (abhinav == "Rock" and anjali == "Scissors") or (abhinav == "Scissors" and anjali == "Paper") or (abhinav == "Paper" and anjali == "Rock"):
    print("Abhinav Wins")
else:
    print("Anjali Wins")