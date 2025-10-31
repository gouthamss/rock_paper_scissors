def computer_selection():
    from random import randint
    options = {1: 'Rock', 2: 'Paper', 3: 'Scissor'}
    computer = randint(1, 3)
    print(f'Computer chose {options[computer]}')
    return computer