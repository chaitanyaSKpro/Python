score1 = 0
score2 = 0
total_rounds = int(input("How many round you want to play: "))

for round_number in range(total_rounds):
    user1 = input("Enter Your Choice: ").lower()
    user2 = input("Enter Your Choice: ").lower()

    if user1 == user2:
        print("The Game is Tie")
    elif user1 == "rock" and user2 == "scissor":
        print("User1 is Win")
        score1 += 1
    elif user1 == "scissor" and user2 =="rock":
        print("User2 is Win")
        score2 += 1
    elif user1 == "rock" and user2 =="paper":
        print("User2 is Win")
        score2 += 1
    elif user1 == "paper" and user2 == "rock":
        print("User1 is Win")
        score1 += 1
    elif user1 == "paper" and user2 == "scissor":
        print("User2 is Win")
        score2 += 1
    elif user1 == "scissor" and user2 == "paper":
        print("User1 is Win")
        score1 += 1 
    else:
        print("Input are invalid , please try again")

print(f"Total Score of User1: {score1}")
print(f"Total Score of User2: {score2}")

if score1 > score2:
    print("User1 is the Winner of the game")
elif score1 == score2:
    print("The game is Tie")
else:
    print("User2 is the Winner of the game")