player_score = 0
computer_score = 0
win_score = 1
computer_put = ''
options = {1: 'Rock', 2: 'Paper', 3: 'Scissor'}

import game_logger as log


def computer_selection():
    from random import randint
    global computer_put
    computer_put = randint(1, 3)
    print(f'Computer chose {options[computer_put]}')
    log.log(f'Computer chose {options[computer_put]}')
    return computer_put


def fight(player, computer):
    if player == computer:
        return 'Draw'
    elif player == 1:
        if computer == 2:
            return 'Computer'
        elif computer == 3:
            return 'Player'
    elif player == 2:
        if computer == 1:
            return 'Player'
        elif computer == 3:
            return 'Computer'
    elif player == 3:
        if computer == 1:
            return 'Computer'
        elif computer == 2:
            return 'Player'
    else:
        print('Invalid input')
        log.log('Invalid input')


def scorecard(result):
    global player_score, computer_score
    if result == 'Player':
        player_score += 1
    elif result == 'Computer':
        computer_score += 1
    print(f'Player score: {player_score}')
    log.log(f'Player score: {player_score}')
    print(f'Computer score: {computer_score}')
    log.log(f'Computer score: {computer_score}')
    if player_score == win_score:
        print('Congratulations! You win')
        log.log('Congratulations! You win')
        return 'Player'
    elif computer_score == win_score:
        print('Better luck next time')
        log.log('Better luck next time')
        return 'Computer'


def new_game():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
