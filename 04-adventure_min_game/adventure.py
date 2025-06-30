name = input("What is your name? ")
print("Welcom", name,"to this adventur")

answer = input("you are on a dirt road, it has come to end and you can go left or right.").lower()

if answer == "left":
     answer = input("you come to a river,you can walk around it or swim").lower()
     if answer == "swim":
         print("you swim across  the river and you were eaten by alligator")
     elif answer == "walk":
         print("you walk across the river, and you get thirsty. while you were drinking water you  were eaten by alligator ")

     else:
         print("Not a valid answer. you lose")

elif answer == "right":
    answer = input("you come to a bridge, it looks wobbly, do you want to cross the road or get back  ").lower()
    if answer == "back":
        print("you go back lose.")
    elif answer == "cross":
        answer = input("hey,look there is a stranger do you want to talk,yes or no  ").lower()
        if answer == "yes":
            print("you talked to the stranger and stranger give u bag of gold and you won!!")
        elif answer == "no":
            print("you igonerd the strnger you lost the bag of gold")
        else:
            print("Not a valid answer. you lose")
    else:
        print("Not a valid answer. you lose")

else:
    print("Not a valid answer. you lose")


print("thanks for playing", name)