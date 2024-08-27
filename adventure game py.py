
welcome=0
won=0

name=input("enter your name: ")
while True:
    if welcome==0:
        print ("welcome", name, "to this adventure")
    else:
        print ("welcome back", name, "to this adventure")
    welcome+=1

    answer= input("You are on a dirt road, it has come to an end and you can go left or right.Which way would you like to go? ")
    if answer == "left":
        answer=input("You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross: ") 

        if answer == "swim":
            print("You swam acrross and were eaten by an alligator.")
        elif answer == "walk":
            print("You walked for many miles, ran out of water and you lost the game.")
        else:
            print('Not a valid option. You lose.')

    elif answer== "right":
        answer=input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")
        if answer == "back":
            print("You go back and lose.")
        elif answer == "cross":
            answer = input("You cross the bridge and meet a stranger. Do you talk to them  (yes/no)? ")
            if answer == "yes":
                print("You talk to the stanger and they give you gold. You WIN!")
                won+=1
            elif answer == "no":
                print("You ignore the stranger and they are offended and you lose.")
            else:
                print('Not a valid option. You lose.')
        else:
            print('Not a valid option. You lose.')
            
        

    else:
        print("please enter a valid statement")
    
    contin=input("enter c to continue and q to quit: ")
    if contin== "c":
        continue
    elif contin=="q":
        print("quit")
        break
    else:
        print("invalid input")
    
print("thank you for trying",  name ,"you won", won,"times in", welcome,"attempt")