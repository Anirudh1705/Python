import random

# Define snakes and ladders
snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

# Function to roll the dice
def roll_dice():
    return random.randint(1, 6)

# Function to move the player
def move_player(player, roll):
    player += roll
    if player in snakes:
        print("Oops! You've been bitten by a snake. You go down from", player, "to", snakes[player])
        player = snakes[player]
    elif player in ladders:
        print("Hooray! You've climbed a ladder. You go up from", player, "to", ladders[player])
        player = ladders[player]
    return player

# Main function to play the game
def play_game():
    player1 = 0
    player2 = 0
    while True:
        input("Player 1: Press Enter to roll the dice")
        roll = roll_dice()
        print("Player 1 rolled:", roll)
        player1 = move_player(player1, roll)
        if player1 >= 100:
            print("Player 1 wins!")
            break
        input("Player 2: Press Enter to roll the dice")
        roll = roll_dice()
        print("Player 2 rolled:", roll)
        player2 = move_player(player2, roll)
        if player2 >= 100:
            print("Player 2 wins!")
            break

# Start the game
play_game()
