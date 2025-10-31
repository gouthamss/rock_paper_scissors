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


scorecard_frame = tk.Frame(root, bg='#4300FF')
scorecard_frame.pack(fill='x', padx=20, pady=20)
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



root.mainloop()
