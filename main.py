from random import randint
import os


def computer_choice(cont):
    computer_chose = randint(0, len(cont) - 1)
    return computer_chose


def user_interface(options):
    for index, option in enumerate(options):
        print(f'{index} = {option}')

    while True:
        user_input = int(input("What do you choose? "))
        if user_input > 2:
            print('Invalid number')
        if not user_input > 2:
            break

    return user_input


def check_results(choices, player, computer):

    if player == computer:
        return "It's a tie!"
    elif (player == 0 and computer == len(choices) - 1) or (
            player > computer and not (player == len(choices) - 1 and computer == 0)):
        return 'Player won!'
    return 'Player lost :('


def play():
    os.system('cls||clear')
    print('''
        -------------------------------
        Welcome to Rock, Paper, Scissors.
        Please pick your weapon. 
        ''')

    option_list = ['Rock', 'Paper', 'Scissors']
    player_result = user_interface(option_list)
    computer_result = computer_choice(option_list)

    print(f'player choose: {option_list[player_result]}')
    print(f'computer choose: {option_list[computer_result]}')

    results = check_results(option_list, player_result, computer_result)
    print(f'\n{results}')


def main():
    play_again = ' '
    while play_again.lower() != 'n':
        play()
        print(f'Do you want to play again? ')
        play_again = input('type \'y\' for yes or \'n\' for no: ')


main()
