print("\n Welcome to Treasure island \n Your Mission is to find the treasure \n")
choice1=input("Enter the Direction you have two choice either Left or Right :")
if choice1 == "Left" :
    choice2 = input("\n You 've come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat."
                    " Type \"swim\" to swim across : ").lower()
    if choice2 == "wait":
        choice3= input("\n You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue."
                       "Which colour do you choose ?").lower()
        if choice3 == "red":
            print(" \n Room full of fire. Game Over")
        elif choice3=="yellow":
            print(" \n You found the treasure. You Win")
        elif choice3 == "blue":
            print(" \n You enter a room of beasts. Game Over")
        else:
            print(" \n You choose a door that doesn't exist. Game Over")
    else:
        print(" \n You got attacked by a trout. Game Over")
else:
    print(" \n You Fell into a hole. Game Over")

