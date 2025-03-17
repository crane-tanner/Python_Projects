import random

min_val = 1
max_val = 6

def roll():
    num = random.randint(min_val, max_val)

    return num

while True:
    print("Welcome to PIG.")
    num_players = input("Choose the number of players (2-4): ")
    if  num_players.isdigit():
        num_players = int(num_players)
        if 2 <= num_players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.\n")

    else:
        print("Invalid, try again.\n")

max_score = 25
players_scores = [0 for _ in range(num_players)]

while max(players_scores) < max_score:
    for player_index in range(num_players):
        print("\nPlayer", player_index + 1, "turn has just started!" )
        print("Your total score is:", players_scores[player_index], "\n")
        current_score = 0

        while True:
            should_role = input("Would you like to roll? (y)")
            if(should_role.lower() != "y"):
                break
            else:
                value = roll()
            if value == 1:
                current_score = 0
                print("You rolled a 1! Turn over.")
                break
            else:
                print("You rolled a ", value)
                current_score += value

            print("Your current score is: ", current_score)

        players_scores[player_index] += current_score
        print("Your total score is: ", players_scores[player_index])

max_score = max(players_scores)
winning_idx = players_scores.index(max_score)
print("Player number",winning_idx+1, "is the winner with a score of:", max_score)