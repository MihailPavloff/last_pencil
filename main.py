import string
players = ['Vici', 'Friday']


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
            break;

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


possible_values = (1, 2, 3)
pencil_amount, current_player = init()

while pencil_amount > 0:
    print(pencil_amount * "|")
    print(f"{players[current_player]}'s turn:")
    taking_pencils = 0
    while True:
        taking_pencils = input()
        if taking_pencils not in '123':
            print("Possible values: '1', '2' or '3'")
            continue
        elif int(taking_pencils) > pencil_amount:
            print("Too many pencils were taken.")
            continue
        taking_pencils = int(taking_pencils)
        break
    pencil_amount -= taking_pencils
    if pencil_amount == 0:
        winner = (current_player + 1) % 2
        print(f"{players[winner]} won!")
    current_player = (current_player + 1) % 2
