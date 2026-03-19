import datetime

now = datetime.datetime.now()


def new_game():
    global now
    now = datetime.datetime.now()
    with open(f'log_{now.strftime('%Y%m%d%H%M%S')}.txt', 'w') as f:
        f.write(f'[{now.strftime('%Y-%m-%d %H:%M:%S')}]: Welcome to the Rock Paper Scissors game\n')


def log(value):
    current = datetime.datetime.now()
    with open(f'log_{now.strftime('%Y%m%d%H%M%S')}.txt', 'a') as f:
        f.write(f'[{current.strftime('%Y-%m-%d %H:%M:%S')}]: {value}\n')
