import random

def nim_game():
    pile_size = random.randint(10, 50)  # Randomly choose pile size
    print("Initial pile size:", pile_size)

    while pile_size > 0:
        player_move = pile_size // 2  # Player picks up 50% of the pile size
        print("You pick up", player_move, "stones.")
        pile_size -= player_move
        print("Remaining stones in pile:", pile_size)

        if pile_size == 0:
            print("Congratulations! You win!")
            break

        computer_move = random.randint(1, min(3, pile_size))
        print("Computer removes", computer_move, "stones.")
        pile_size -= computer_move
        print("Remaining stones in pile:", pile_size)

        if pile_size == 0:
            print("Sorry, you lost. Better luck next time!")
            break

nim_game()
