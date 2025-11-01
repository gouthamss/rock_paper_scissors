import tkinter as tk
from logics import computer_selection


def toggle_fullscreen(event=None):
    current_state = root.attributes('-fullscreen')
    root.attributes('-fullscreen', not current_state)


root = tk.Tk()
root.title('Rock Paper Scissors Game')
root.geometry("400x300")
root.attributes('-fullscreen', True)

root.bind('<F11>', toggle_fullscreen)
root.bind('<Escape>', lambda e: root.attributes('-fullscreen', False))


def game():
    # only call other functions/methods from logics.py from here
    pass


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
rock_selection = tk.Button(player_selection_frame, text='\nROCK\n', fg='white', bg='#B87C4C')
rock_selection.grid(row=0, column=0, sticky='NEWS', padx=20, pady=10)
paper_selection = tk.Button(player_selection_frame, text='\nPAPER\n', fg='white', bg='#C4A484')
paper_selection.grid(row=0, column=1, sticky='NEWS', padx=20, pady=10)
scissors_selection = tk.Button(player_selection_frame, text='\nSCISSORS\n', fg='black', bg='#F7F1DE')
scissors_selection.grid(row=0, column=2, sticky='NEWS', padx=20, pady=10)
submit_button = tk.Button(player_selection_frame, text='Submit')
submit_button.grid(row=1, column=1, pady=10)

# fight frame
fight_frame = tk.Frame(root, bg='#703B3B')
fight_frame.pack(fill='x', padx=20, pady=10)
fight_frame.grid_columnconfigure(0, weight=1)
fight_frame.grid_columnconfigure(1, weight=1)
fight_frame.grid_columnconfigure(2, weight=1)
player_selection = tk.Label(fight_frame, text='', fg='white', bg='#703B3B')
player_selection.grid(row=0, column=0, sticky='NEWS', padx=20, pady=10)
vs = tk.Label(fight_frame, text='--VS--', fg='white', bg='#703B3B')
vs.grid(row=0, column=0, sticky='NEWS', padx=20, pady=10)
comp_selection = tk.Label(fight_frame, text='', fg='white', bg='#703B3B')
comp_selection.grid(row=0, column=0, sticky='NEWS', padx=20, pady=10)

# results frame
results_frame = tk.Frame(root)
results_frame.pack(fill='x', padx=20, pady=10)
result = tk.Label(results_frame, text='', fg='#703B3B', bg='white')
result.pack(fill='x', padx=20, pady=10)


root.mainloop()
