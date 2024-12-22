import random


def rock_scissor_paper(player_move, opponent_move):

    player_move = player_move.lower()
    opponent_move = opponent_move.lower()

    result = False

    if player_move == "rock" and opponent_move == "scissor":
        result = True
    elif player_move == "paper" and opponent_move == "rock":
        result = True
    elif player_move == "scissor" and opponent_move == "paper":
        result = True

    return result


def random_number():
    random_number_1 = random.randint(0, 2)
    random_number_2 = random.randint(0, 2)
    return [random_number_1, random_number_2]


while True:
    start_quit = input("Start Or Quit The Game: Y/Q: ")
    if start_quit == "Y":
        items = ["rock", "paper", "scissor"]
        [random_number_1, random_number_2] = random_number()
        print(
            "Values picked by players: " + items[random_number_1],
            items[random_number_2],
        )
        player_one = items[random_number_1]
        player_two = items[random_number_2]

        result = rock_scissor_paper(player_one, player_two)
        if result:
            print("Player one won!")
        else:
            print("Player two won!")
    elif start_quit == "Q":
        break
