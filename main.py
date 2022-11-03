import string
import turns


players = ['Vici', 'Friday']
possible_values = (1, 2, 3)


def init():
    print("How many pencils would you like to use:")
    while True:
        amount = input()
        error_flag = 0
        if amount.lstrip('-') == "" or amount.lstrip("+") == "":
            print("The number of pencils should be numeric")
            continue
        for sym in amount.lstrip('-'):
            if sym not in string.digits:
                print("The number of pencils should be numeric")
                error_flag = 1
        if error_flag:
            continue
        elif int(amount) <= 0:
            print("The number of pencils should be positive")
            continue
        else:
            break

    print("Who will be the first (Vici, Friday):")
    while True:
        name = input()
        if name not in players:
            print(f'Choose between {players[0]} and {players[1]}')
            continue
        break
    if name == players[0]:
        index = 0
    else:
        index = 1
    return int(amount), index


pencil_amount, current_player = init()

while pencil_amount > 0:
    print(pencil_amount * "|")
    print(f"{players[current_player]}'s turn:")
    taking_pencils = 0
    while True:
        if current_player == 0:
            taking_pencils = turns.player_turn(pencil_amount)
            if taking_pencils:
                break
        else:
            taking_pencils = turns.bot_turn(pencil_amount)
            print(taking_pencils)
            break

    pencil_amount -= taking_pencils
    if pencil_amount == 0:
        winner = (current_player + 1) % 2
        print(f"{players[winner]} won!")
    current_player = (current_player + 1) % 2
