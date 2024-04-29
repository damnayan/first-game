import random
def roll():
    min_value = 1 
    max_value = 6
    roll = random.randint(min_value, max_value)
    
    return roll

while True:
    players = input("enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if (players >=2 and players <= 4):
            break
        else:
            print("Must be beetween 2 - 4 players")
    else:
        print("Not valid number of players")
max_score = 50
player_scores= [0 for _ in range(players)]

while max(player_scores) < max_score:

    for play_indx in range(players):
        print("\nPlayer number", play_indx + 1, "turn has just started!\n")
        print("Your total score is :", player_scores[play_indx], "\n")
        current_score = 0


        while True:
                should_roll = input("Would you like to roll(y)? ")
                if should_roll.lower() != "y":
                    break
                value = roll()
                if (value == 1):
                    print("the end. you rolled a 1 in the dice")
                    current_score = 0
                    break
                else:
                    current_score += value
                    print(f"You rolled a {value}")
        
                print(f"Your current score is: {current_score}")

        player_scores[play_indx] += current_score
        print("Your total score is :", player_scores[play_indx])

win_score = max(player_scores)
winning_indx = player_scores.index(win_score)
print("Player ", winning_indx +1 , "won this game with the score of ", win_score)

