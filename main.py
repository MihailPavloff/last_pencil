import string
players = ['Vici', 'Friday']


def init():
    print("How many pencils would you like to use:")
    while True:
        amount = input()
        for sym in amount:
            if sym not in string.digits:
                print("The number of pencils should be numeric")
        if amount <= 0:
            print("The number of pencils should be positive")
        else:
            break;

    print("Who will be the first (Vici, Friday):")
    while True:
        name = input()
        if name not in players:
            print(f'Choose between {players[0]} and {players[1]}')
        break
    if name == players[0]:
        index = 0
    else:
        index = 1
    return amount, index


possible_values = (1, 2, 3)
pencil_amount, current_player = init()

while pencil_amount > 0:
    print(pencil_amount * "|")
    print(f"{players[current_player]}'s turn:")
    current_player = (current_player + 1) % 2
    taking_pencils = 0
    while taking_pencils not in possible_values and taking_pencils <= pencil_amount:
        taking_pencils = int(input())
        if taking_pencils not in (1, 2, 3):
            print("Possible values: '1', '2' or '3'")
        elif taking_pencils > pencil_amount:
            print("Too many pencils were taken.")
    pencil_amount -= taking_pencils
