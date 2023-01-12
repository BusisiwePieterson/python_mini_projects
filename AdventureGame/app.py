name  = input("Type your name: ")
print("Welcome", name, "to the adventure!")


answer = input("You have come to a dirt road which way would you like to go? left or right: ").lower()

if answer == "left":
    print("You have come to a river, would you like to walk or swim across? ")
    if answer == "swim":
        print("You swam across and were eaten by a shark.")
    elif answer == "walk":
        print("You walked and got tired ad lost the game.")
    else:
        print("You lose, not a valid option")


elif answer == "right":
    print("You have come to a brigde and it looks wobbly, what is your next move? cross/back? ")
    if answer == "back":
        print("You went back and have lost.")
    elif answer == "cross":
        print("You cross the brigde and see a homeless stranger, will you talk to him? Yes/No ")
        if answer == "yes":
            print("You greeted homeless man, he gave you gold, and so you win")
        elif answer == "no":
            print("You ignored the homeless man and you lose")
        else:
            print("not a valid option you lose!")

    else:
        print("You lose, not a valid option")


else:
    print("Not a valid option")

print(f"Thank you for playing {name}")