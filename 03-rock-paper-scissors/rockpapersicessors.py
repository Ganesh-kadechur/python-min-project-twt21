import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissor"]

while True:
    user_input = input("type you want to choose whether rock, paper, or scissor to quit the press q : ").lower()
    if user_input == "q":
        break


    if user_input not in  options:
        print("please enter a valid choice")
        continue

    random_number = random.randint(0, 2)
    # rock is 0 , paper 1 , scissor 2
    computer_pick = options[random_number]
    print("computer picked " , computer_pick +".")

    if user_input == "rock" and computer_pick == "scissor":
        print("you won!")
        user_wins += 1
        continue

    elif user_input == "paper" and computer_pick == "rock":
        print("you won!")
        user_wins += 1
        continue

    elif user_input == "scissor" and computer_pick == "paper":
        print("you won!")
        user_wins += 1
        continue

    elif user_input == computer_pick:
        print("its tie")

    else:
        print("you lost")
        computer_wins += 1

print("you won " +  str(user_wins) + " times")
print("computer won "+str(computer_wins)+ " times")


print("goodbye")



