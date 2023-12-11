import tkinter as tk
from tkinter import messagebox

class Morpion:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Morpion")
        
        self.current_player = 'X'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                button = tk.Button(self.window, text='', font=('normal', 20), width=5, height=2,
                                   command=lambda row=i, col=j: self.on_button_click(row, col))
                button.grid(row=i, column=j)

    def on_button_click(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.update_button(row, col)
            
            if self.check_winner(row, col):
                messagebox.showinfo("Victoire", f"Le joueur {self.current_player} a gagné !")
                self.reset_game()
            elif self.is_board_full():
                messagebox.showinfo("Match nul", "La partie est un match nul.")
                self.reset_game()
            else:
                self.switch_player()

    def update_button(self, row, col):
        button = self.window.grid_slaves(row=row, column=col)[0]
        button.config(text=self.current_player, state=tk.DISABLED)

    def check_winner(self, row, col):
        # Vérifier les lignes, colonnes et diagonales
        return (self.check_row(row) or
                self.check_column(col) or
                self.check_diagonals())

    def check_row(self, row):
        return all(self.board[row][i] == self.current_player for i in range(3))

    def check_column(self, col):
        return all(self.board[i][col] == self.current_player for i in range(3))

    def check_diagonals(self):
        return (all(self.board[i][i] == self.current_player for i in range(3)) or
                all(self.board[i][2 - i] == self.current_player for i in range(3)))

    def is_board_full(self):
        return all(self.board[i][j] != ' ' for i in range(3) for j in range(3))

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def reset_game(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        for button in self.window.grid_slaves():
            button.config(text='', state=tk.NORMAL)

if __name__ == "__main__":
    game = Morpion()
    game.window.mainloop()


