import random
def roll():
    min_num= 1
    max_num= 6
    roll= random.randint(min_num, max_num)
    return roll
while True:
    player=input("enter the number of player[2-4]: ")
    if player.isdigit():
        player= int(player)
        if 2<= player <= 4:
            break
        else:
            print("! please enter a number between 2 and4 ")
    else:
        print("enter a valid input!")
max_score = 50
player_score = [0 for i in range (player)]
while max(player_score)< max_score:
    for player_idx in range(player):
        print("\nplayer no", player_idx +1,"\n")
        print("\nyour current score is ", player_score[player_idx],"\n")
        current_score=0
        while True:
            should_roll= input("do you like to rool dice, type 'y' to rool:  ").lower()
            if should_roll!= "y":
                break
            value= roll()
            if value== 1:
                print("you rooled a 1, your turn completed")
                current_score=0
                break
            else:
                current_score+= value
                print("you rooled a ", value)
            print("your  score is ",current_score )
        player_score[player_idx]+= current_score
        print("your current score is ", player_score[player_idx])
        
max_score= max(player_score)
winning_idx= player_score.index(max_score)
print("player no ", winning_idx+1,"is the winner with the score of ", max_score)