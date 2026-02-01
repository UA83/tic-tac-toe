import tkinter as tk
from tkinter import messagebox, colorchooser, Toplevel

class TicTacToeLogic:
    def __init__(self):
        self.current_player = "X"
        self.board = [""] * 9
        self.winner = None
        self.game_over = False
        self.winning_combo = None
        self.scores = {"X": 0, "O": 0}

    def reset_scores(self):
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


        self.colors = {
            "bg": "#2C3E50",
            "btn_bg": "#34495E",
            "text": "#ECF0F1",
            "X": "#E74C3C",
            "O": "#3498DB",
            "win": "#2ECC71"
        }

        self.root.configure(bg=self.colors["bg"])
        
        self.score_frame = tk.Frame(self.root, bg=self.colors["bg"])
        self.score_frame.grid(row=0, column=0, columnspan=3, pady=(10, 5))

        self.score_label_x = tk.Label(self.score_frame, text="X: 0", 
                                    font=('Helvetica', 16, 'bold'), 
                                    bg=self.colors["bg"], fg=self.colors["X"])
        self.score_label_x.pack(side="left", padx=10)

        self.score_label_o = tk.Label(self.score_frame, text="O: 0", 
                                    font=('Helvetica', 16, 'bold'), 
                                    bg=self.colors["bg"], fg=self.colors["O"])
        self.score_label_o.pack(side="left", padx=10)
        
        self.score_label_o.pack(side="left", padx=10)
        
        # self.create_menu() # Removed native menu
        self.create_widgets()
    
    # create_menu removed

    def open_settings(self):
        settings_win = Toplevel(self.root)
        settings_win.title("Settings")
        settings_win.configure(bg=self.colors["bg"])
        settings_win.geometry("300x200")
        
        lbl = tk.Label(settings_win, text="Player Colors", font=('Helvetica', 14, 'bold'),
                       bg=self.colors["bg"], fg=self.colors["text"])
        lbl.pack(pady=10)
        
        btn_x = tk.Button(settings_win, text="Color for X", font=('Helvetica', 12),
                          bg=self.colors["btn_bg"], fg=self.colors["text"],
                          relief="flat", width=15,
                          command=lambda: self.choose_color_x(settings_win))
        btn_x.pack(pady=5)

        btn_o = tk.Button(settings_win, text="Color for O", font=('Helvetica', 12),
                          bg=self.colors["btn_bg"], fg=self.colors["text"],
                          relief="flat", width=15,
                          command=lambda: self.choose_color_o(settings_win))
        btn_o.pack(pady=5)

        close_btn = tk.Button(settings_win, text="Close", font=('Helvetica', 10),
                              bg="#E74C3C", fg=self.colors["text"],
                              activebackground="#C0392B", activeforeground=self.colors["text"],
                              relief="flat", width=10,
                              command=settings_win.destroy)
        close_btn.pack(pady=15)
    
    # choose_color_x and choose_color_o modified to take parent

    def choose_color_x(self, parent=None):
        color = colorchooser.askcolor(title="Choose color for X", parent=parent)[1]
        if color:
            self.colors["X"] = color
            self.update_board_colors()

    def choose_color_o(self, parent=None):
        color = colorchooser.askcolor(title="Choose color for O", parent=parent)[1]
        if color:
            self.colors["O"] = color
            self.update_board_colors()

    def update_board_colors(self):
        for i, btn in enumerate(self.buttons):
            player = self.game.board[i]
            if player == "X":
                btn.config(fg=self.colors["X"])
            elif player == "O":
                btn.config(fg=self.colors["O"])
        
        
        self.score_label_x.config(fg=self.colors["X"])
        self.score_label_o.config(fg=self.colors["O"])
        
        # Also update reset button logic (if we want reset button to match active player or X)
        pass

    
    def create_widgets(self):
        for i in range(9):
            btn = tk.Button(self.root, text="", font=('Helvetica', 24, 'bold'), height=2, width=5,
                            bg=self.colors["btn_bg"], fg=self.colors["text"],
                            activebackground=self.colors["bg"], activeforeground=self.colors["text"],
                            relief="flat", borderwidth=0,
                            command=lambda i=i: self.on_button_click(i))
            btn.grid(row=(i // 3) + 1, column=i % 3, padx=2, pady=2)
            self.buttons.append(btn)
        
        # Removed default_btn_bg capture as we use defined colors now

        # Control buttons frame
        ctrl_frame = tk.Frame(self.root, bg=self.colors["bg"])
        ctrl_frame.grid(row=4, column=0, columnspan=3, pady=(10, 10))

        reset_btn = tk.Button(ctrl_frame, text="Reset Game", font=('Helvetica', 10, 'bold'),
                              bg=self.colors["btn_bg"], fg=self.colors["text"],
                              relief="flat", width=10,
                              command=self.reset_game)
        reset_btn.pack(side="left", padx=5)

        reset_score_btn = tk.Button(ctrl_frame, text="Reset Score", font=('Helvetica', 10, 'bold'),
                                    bg=self.colors["btn_bg"], fg=self.colors["text"],
                                    relief="flat", width=10,
                                    command=self.reset_scores)
        reset_score_btn.pack(side="left", padx=5)

        settings_btn = tk.Button(ctrl_frame, text="Settings", font=('Helvetica', 10, 'bold'),
                                 bg=self.colors["btn_bg"], fg=self.colors["text"],
                                 relief="flat", width=8,
                                 command=self.open_settings)
        settings_btn.pack(side="left", padx=5)

    def reset_scores(self):
        self.game.reset_scores()
        self.update_score_label()

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
        self.score_label_x.config(text=f"X: {scores['X']}")
        self.score_label_o.config(text=f"O: {scores['O']}")

    def update_ui(self, index):
        player = self.game.board[index]
        color = self.colors["X"] if player == "X" else self.colors["O"]
        self.buttons[index].config(text=player, fg=color)

    def highlight_winner(self):
        if self.game.winning_combo:
            winner = self.game.winner
            win_color = self.colors["X"] if winner == "X" else self.colors["O"]
            for index in self.game.winning_combo:
                self.buttons[index].config(bg=win_color, fg="white")

    def reset_game(self):
        self.game.reset()
        for btn in self.buttons:
            btn.config(text="", bg=self.colors["btn_bg"])

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()
