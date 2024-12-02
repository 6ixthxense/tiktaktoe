import tkinter as tk
from tkinter import messagebox

# Initialize variables
board = [' ' for _ in range(9)]
player = 'X'
ai = 'O'

# Win conditions
win_conditions = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
]

# Function to check for a win
def check_win(symbol):
    for condition in win_conditions:
        if all(board[i] == symbol for i in condition):
            return True
    return False

# Function for AI move
# Function for AI move
def ai_move():
    # Rule 1: Win if possible
    for i in range(9):
        if board[i] == ' ':
            board[i] = ai
            if check_win(ai):
                return
            board[i] = ' ' 

    # Rule 2: Block the player from winning
    for i in range(9):
        if board[i] == ' ':
            board[i] = player
            if check_win(player):
                board[i] = ai
                return
            board[i] = ' '

    # Rule 3: Special block cases (0, 7, 6, 8 case)
    if board[0] == player and board[7] == player and board[3] == ' ':
        board[3] = ai
        return
    if board[6] == player and board[8] == player and board[5] == ' ':
        board[5] = ai
        return

    # Rule 4: Detect and block Fork
    for i in [1, 3, 5, 7]:
        if board[i] == ' ' and (
            (board[0] == player and board[8] == player) or
            (board[2] == player and board[6] == player)
        ):
            board[i] = ai
            return

    # Rule 5: Take the center if available
    if board[4] == ' ':
        board[4] = ai
        return

    # Rule 6: Take any corner if available
    for i in [0, 2, 6, 8]:
        if board[i] == ' ':
            board[i] = ai
            return

    # Rule 7: Take any side if available
    for i in [1, 3, 5, 7]:
        if board[i] == ' ':
            board[i] = ai
            return


# Function to update buttons
def update_buttons():
    for i in range(9):
        buttons[i].config(text=board[i],
                          fg="blue" if board[i] == 'X' else "red" if board[i] == 'O' else "black")
    if check_win(player):
        messagebox.showinfo("Game Over", "Congratulations! You win!")
        root.destroy()
    elif check_win(ai):
        messagebox.showinfo("Game Over", "AI wins! Better luck next time.")
        root.destroy()
    elif ' ' not in board:
        messagebox.showinfo("Game Over", "It's a draw!")
        root.destroy()

# Function for player move
def player_click(index):
    if board[index] == ' ':
        board[index] = player
        update_buttons()
        if not check_win(player) and ' ' in board:
            ai_move()
            update_buttons()

# Function to restart the game
def restart_game():
    global board
    board = [' ' for _ in range(9)]
    for btn in buttons:
        btn.config(text=' ', state='normal')

# Create the GUI
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Create buttons
buttons = []
for i in range(9):
    btn = tk.Button(root, text=' ', font=('Arial', 20), height=2, width=5,
                    command=lambda i=i: player_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)


# Run the GUI
root.mainloop()

