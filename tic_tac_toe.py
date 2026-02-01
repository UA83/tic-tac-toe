import tkinter as tk
from tkinter import messagebox

class TicTacToeLogic:
    def __init__(self):
        self.current_player = "X"
        self.board = [""] * 9
        self.winner = None
        self.game_over = False
        self.winning_combo = None
        self.scores = {"X": 0, "O": 0}

    def make_move(self, index):
        if self.board[index] == "" and not self.game_over:
            self.board[index] = self.current_player
            if self.check_winner():
                self.game_over = True
                self.winner = self.current_player
                self.scores[self.current_player] += 1
            elif "" not in self.board:
                self.game_over = True
                self.winner = "Draw"
            else:
                self.switch_player()
            return True
        return False

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)              # Diagonals
        ]

        for a, b, c in winning_combinations:
            if self.board[a] == self.board[b] == self.board[c] and self.board[a] != "":
                self.winning_combo = (a, b, c)
                return True
        return False

    def reset(self):
        if self.winner and self.winner != "Draw":
            self.current_player = self.winner
        else:
            self.current_player = "X"
            
        self.board = [""] * 9
        self.winner = None
        self.game_over = False
        self.winning_combo = None

class TicTacToeGUI:
    def __init__(self, root):
        self.game = TicTacToeLogic()
        self.root = root
        self.root.title("Tic Tac Toe")
        self.buttons = []


        self.root.configure(bg='lightblue')
        
        self.score_label = tk.Label(self.root, text="Score - X: 0 | O: 0", font=('Arial', 14), bg='lightblue')
        self.score_label.grid(row=0, column=0, columnspan=3, pady=5)
        
        self.create_widgets()
    
    def create_widgets(self):
        for i in range(9):
            btn = tk.Button(self.root, text="", font=('Arial', 20), height=3, width=6,
                            command=lambda i=i: self.on_button_click(i))
            btn.grid(row=(i // 3) + 1, column=i % 3, padx=5, pady=5)
            self.buttons.append(btn)
        
        self.default_btn_bg = self.buttons[0].cget('bg')

        reset_btn = tk.Button(self.root, text="Reset Game", font=('Arial', 12), command=self.reset_game)
        reset_btn.grid(row=4, column=0, columnspan=3, sticky="we", padx=5, pady=5)

    def on_button_click(self, index):
        if self.game.make_move(index):
            self.update_ui(index)
            
            if self.game.game_over:
                if self.game.winner == "Draw":
                    messagebox.showinfo("Game Over", "It's a draw!")
                    self.reset_game()
                else:
                    self.highlight_winner()
                    self.update_score_label()
                    messagebox.showinfo("Game Over", f"Player {self.game.winner} wins!")
                self.reset_game()
    
    def update_score_label(self):
        scores = self.game.scores
        self.score_label.config(text=f"Score - X: {scores['X']} | O: {scores['O']}")

    def update_ui(self, index):
        self.buttons[index].config(text=self.game.board[index])

    def highlight_winner(self):
        if self.game.winning_combo:
            for index in self.game.winning_combo:
                self.buttons[index].config(bg="lightgreen")

    def reset_game(self):
        self.game.reset()
        for btn in self.buttons:
            btn.config(text="", bg=self.default_btn_bg)

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()
