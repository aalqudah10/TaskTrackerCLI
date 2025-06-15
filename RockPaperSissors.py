import random

while True:
    user_choice = input("Please enter your choice: ")
    possible_choices = ['rock','paper','scissor']
    computer_choice = random.choice(possible_choices)
    while user_choice.lower() not in possible_choices:
            user_choice = input("Wrong Choice, please try again")

    print(f'You chose: {user_choice.upper()}')
    print(f'Computer chose: {computer_choice.upper()}')
    if user_choice.lower() == computer_choice:
        print(f'Both users selected {user_choice.upper()}, it\'s a tie!')
    elif user_choice.lower() == 'rock':
        if computer_choice == 'paper':
            print(f'{computer_choice.upper()} covers {user_choice.upper()}. You\'ve lost!')
        else:
            print(f'{user_choice.upper()} breaks {computer_choice.upper()}. You\'ve won!')
    elif user_choice.lower() == 'scissor':
        if computer_choice == 'rock':
            print(f'{computer_choice.upper()} breaks {user_choice.upper()}. You\'ve lost!')
        else:
            print(f'{user_choice.upper()} cuts {computer_choice.upper()}. You\'ve won!')
    else:
        if computer_choice == 'rock':
            print(f'{user_choice.upper()} covers {computer_choice.upper()}. You\'ve won!')
        else:
            print(f'{computer_choice.upper()} cuts {user_choice.upper()}. You\'ve lost!')

    is_yes = input('Do you want to play again? (y/n): ')
    if is_yes.lower() != 'y':
        break

