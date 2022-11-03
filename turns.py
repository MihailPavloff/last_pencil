import random


def bot_turn(pencil_amount):
    if pencil_amount % 4 == 1:
        if pencil_amount != 1:
            return random.randint(1, 3)
        return 1
    else:
        return (pencil_amount - 1) % 4


def player_turn(pencil_amount):
    pencils = input()
    if pencils not in '123':
        print("Possible values: '1', '2' or '3'")
        return False
    elif int(pencils) > pencil_amount:
        print("Too many pencils were taken.")
        return False
    pencils = int(pencils)
    return pencils
