import tkinter as tk
from tkinter import messagebox

class TicTacToeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []
        self.game_over = False

        self.root.configure(bg='lightblue')
        self.create_widgets()

    def create_widgets(self):
        for i in range(9):
            btn = tk.Button(self.root, text="", font=('Arial', 20), height=3, width=6,
                            command=lambda i=i: self.on_button_click(i))
            btn.grid(row=i // 3, column=i % 3)
            self.buttons.append(btn)
        
        self.default_btn_bg = self.buttons[0].cget('bg')

        reset_btn = tk.Button(self.root, text="Reset Game", font=('Arial', 12), command=self.reset_game)
        reset_btn.grid(row=3, column=0, columnspan=3, sticky="we")

    def on_button_click(self, index):
        if self.board[index] == "" and not self.game_over:
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.game_over = True
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a draw!")
                self.game_over = True
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)              # Diagonals
        ]

        for a, b, c in winning_combinations:
            if self.board[a] == self.board[b] == self.board[c] and self.board[a] != "":
                self.highlight_winner(a, b, c)
                return True
        return False

    def highlight_winner(self, a, b, c):
        for index in [a, b, c]:
            self.buttons[index].config(bg="lightgreen")

    def reset_game(self):
        self.current_player = "X"
        self.board = [""] * 9
        self.game_over = False
        for btn in self.buttons:
            btn.config(text="", bg=self.default_btn_bg)

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGame(root)
    root.mainloop()
