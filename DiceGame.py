import random

def roll():
    min_val = 1
    max_val = 6
    roll = random.randint(min_val,max_val)
    
    return roll

while True:
    players = input("Enter the number of players : ")
    if players.isdigit():
        players = int(players)
        if 1 < players <= 40 :
            break
        else:
            print("Must be between 2-40 players.")
    elif players.lower() == "n":
        break
    
    else:
        print("Invalid input , Try again!!")

max_score = 50
player_scores = [0 for _ in range (players)]

while max(player_scores) < max_score:
    
    for player_ind in range(players):
        print("\nPlayer ",player_ind+1," turn has started !!")
        print("Your total score is: ",player_scores[player_ind],"\n")
        current_score=0
        
        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break
            
            value = roll()
            if value == 1:
                print("You rolled 1!! Turn completed!!")
                current_score = 0
                break
            
            else:
                current_score += value
                print("You rolled a: ",value)
            
            print("Your score is: ",current_score)
        
        player_scores[player_ind] += current_score
        print("Your total score is : ",player_scores[player_ind])

max_score = max(player_scores)
win_idx = player_scores.index(max_score)
print("Player ",win_idx+1," is the winner with a score of : ",max_score)