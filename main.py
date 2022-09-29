print("How many pencils would you like to use:")
pencil_amount = int(input())

print("Who will be the first (Vici, Friday):")
first_player = input()

while pencil_amount > 0:
    print(pencil_amount * "|")
    print(f"{first_player}'s turn:")
    if first_player == 'Vici':
        first_player = 'Friday'
    elif first_player == 'Friday':
        first_player = 'Vici'
    pencil_amount -= int(input())

