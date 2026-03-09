import tkinter as tk
import logics


def toggle_fullscreen(event=None):
    current_state = root.attributes('-fullscreen')
    root.attributes('-fullscreen', not current_state)


root = tk.Tk()
root.title('Rock Paper Scissors Game')
root.geometry("400x350")
root.configure(bg='#FFFFFF')
# root.attributes('-fullscreen', True)

root.bind('<F11>', toggle_fullscreen)
root.bind('<Escape>', lambda e: root.attributes('-fullscreen', False))

player_selected = 0
game_won = 0


def player_rock():
    global player_selected
    player_selected = 1
    submit_button.config(state=tk.NORMAL)
    print('Player chose Rock')
    return player_selected


def player_paper():
    global player_selected
    player_selected = 2
    submit_button.config(state=tk.NORMAL)
    print('Player chose Paper')
    return player_selected


def player_scissors():
    global player_selected
    player_selected = 3
    submit_button.config(state=tk.NORMAL)
    print('Player chose Scissors')
    return player_selected


def new_game():
    global game_won
    rock_selection.config(state=tk.NORMAL)
    paper_selection.config(state=tk.NORMAL)
    scissors_selection.config(state=tk.NORMAL)
    submit_button.grid()
    submit_button.config(state=tk.DISABLED)
    new_game_button.grid_remove()
    logics.new_game()
    root.configure(bg='#FFFFFF')
    result_announce.configure(text='',fg='#FFFFFF')
    player_selection_text.configure(text='')
    comp_selection_text.configure(text='')
    scorecard_player_score.configure(text=logics.player_score)
    scorecard_computer_score.configure(text=logics.computer_score)
    game_won = 0


def game():
    # only call other functions/methods from logics.py from here
    global game_won
    if game_won == 0:
        computer = logics.computer_selection()
        result = logics.fight(player_selected, computer)
        print(f'{result} wins this round')
        score = logics.scorecard(result)
        player_selection_text.configure(text=logics.options[player_selected])
        comp_selection_text.configure(text=logics.options[logics.computer_put])
        scorecard_player_score.configure(text=logics.player_score)
        scorecard_computer_score.configure(text=logics.computer_score)
        if score is not None:
            game_won = 1
            submit_button.grid_remove()
            new_game_button.grid()
            rock_selection.config(state=tk.DISABLED)
            paper_selection.config(state=tk.DISABLED)
            scissors_selection.config(state=tk.DISABLED)
            root.configure(bg='#00FF00' if score == 'Player' else '#FF0000')
            result_announce.configure(text=f'{score} wins this game', fg='#00FF00' if score == 'Player' else '#FF0000')
            print(f'{score} wins this game')


# scorecard
scorecard_frame = tk.Frame(root, bg='#4300FF')
scorecard_frame.pack(fill='x', padx=20, pady=10)
scorecard_label = tk.Label(scorecard_frame, text='SCORECARD:', bg='#4300FF', fg='white', font=("Arial", 24, "bold"))
scorecard_label.pack(side='top', fill='x')
scorecard_player = tk.Label(scorecard_frame, text='PLAYER:', bg='#4300FF', fg='white', font=("Arial", 16, "bold"))
scorecard_player.pack(side='left')
scorecard_player_score = tk.Label(scorecard_frame, text='0', bg='#4300FF', fg='white', font=("Arial", 16, "bold"))
scorecard_player_score.pack(side='left')
scorecard_computer_score = tk.Label(scorecard_frame, text='0', bg='#4300FF', fg='white', font=("Arial", 16, "bold"))
scorecard_computer_score.pack(side='right')
scorecard_computer = tk.Label(scorecard_frame, text='COMPUTER:', bg='#4300FF', fg='white', font=("Arial", 16, "bold"))
scorecard_computer.pack(side='right')

# player selection
player_selection_frame = tk.Frame(root, bg='#4300FF')
player_selection_frame.pack(fill='x', padx=20, pady=10)
player_selection_frame.grid_columnconfigure(0, weight=1)
player_selection_frame.grid_columnconfigure(1, weight=1)
player_selection_frame.grid_columnconfigure(2, weight=1)
rock_selection = tk.Button(player_selection_frame, text='\n   ROCK   \n', fg='white', bg='#B87C4C', command=player_rock)
rock_selection.grid(row=0, column=0, sticky='NEWS', padx=(10, 5), pady=10)
paper_selection = tk.Button(player_selection_frame, text='\n  PAPER  \n', fg='white', bg='#C4A484', command=player_paper)
paper_selection.grid(row=0, column=1, sticky='NEWS', padx=(5, 5), pady=10)
scissors_selection = tk.Button(player_selection_frame, text='\nSCISSORS\n', fg='black', bg='#F7F1DE', command=player_scissors)
scissors_selection.grid(row=0, column=2, sticky='NEWS', padx=(5, 10), pady=10)
submit_button = tk.Button(player_selection_frame, text='Submit', command=game)
submit_button.grid(row=1, column=1, pady=(0, 10))
submit_button.config(state=tk.DISABLED)
new_game_button = tk.Button(player_selection_frame, text='New Game', command=new_game)
new_game_button.grid(row=1, column=1, pady=(0, 10))
new_game_button.grid_remove()

# fight frame
fight_frame = tk.Frame(root, bg='#703B3B')
fight_frame.pack(fill='x', padx=20, pady=10)
fight_frame.grid_columnconfigure(0, weight=1)
fight_frame.grid_columnconfigure(1, weight=1)
fight_frame.grid_columnconfigure(2, weight=1)
player_selection_text = tk.Label(fight_frame, text='', fg='white', bg='#703B3B')
player_selection_text.grid(row=0, column=0, sticky='NEWS', padx=20, pady=10)
vs = tk.Label(fight_frame, text='--VS--', fg='white', bg='#703B3B')
vs.grid(row=0, column=1, sticky='NEWS', padx=20, pady=10)
comp_selection_text = tk.Label(fight_frame, text='', fg='white', bg='#703B3B')
comp_selection_text.grid(row=0, column=2, sticky='NEWS', padx=20, pady=10)

# results frame
results_frame = tk.Frame(root, bg='#703B3B')
results_frame.pack(fill='x', padx=20, pady=10)
result_announce = tk.Label(results_frame, text='', fg='white', bg='#703B3B', font=("Arial", 16, "bold"))
result_announce.pack(fill='x', padx=20, pady=10)

root.mainloop()
