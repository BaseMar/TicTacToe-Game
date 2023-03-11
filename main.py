import tkinter as tk
from tkinter import messagebox


class TicTacToeModel:
    def __init__(self):
        self.board = [' '] * 9
        self.turn = 'X'

    def make_move(self, index):
        if self.board[index] == ' ':
            self.board[index] = self.turn
            if self.check_win():
                return f'Player {self.turn} wins!'
            elif self.check_tie():
                return 'Tie Game!'
            else:
                self.change_turn()
                return None
        else:
            return 'Invalid move'

    def check_win(self):
        if (self.board[0] == self.board[1] == self.board[2] != ' ') or \
                (self.board[3] == self.board[4] == self.board[5] != ' ') or \
                (self.board[6] == self.board[7] == self.board[8] != ' ') or \
                (self.board[0] == self.board[3] == self.board[6] != ' ') or \
                (self.board[1] == self.board[4] == self.board[7] != ' ') or \
                (self.board[2] == self.board[5] == self.board[8] != ' ') or \
                (self.board[0] == self.board[4] == self.board[8] != ' ') or \
                (self.board[2] == self.board[4] == self.board[6] != ' '):
            return True
        else:
            return False

    def check_tie(self):
        if ' ' not in self.board:
            return True
        else:
            return False

    def change_turn(self):
        if self.turn == 'X':
            self.turn = 'O'
        else:
            self.turn = 'X'


class TicTacToeView:
    def __init__(self, master, controller):
        self.master = master
        self.controller = controller
        self.buttons = []
        for i in range(9):
            button = tk.Button(self.master, text=' ', font=('Arial', 20), width=4, height=2,
                               command=lambda i=i: self.controller.make_move(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def update(self, board):
        for i in range(9):
            self.buttons[i]['text'] = board[i]


class TicTacToeController:
    def __init__(self):
        self.model = TicTacToeModel()
        self.root = tk.Tk()
        self.view = TicTacToeView(self.root, self)
        self.root.mainloop()

    def make_move(self, index):
        result = self.model.make_move(index)
        if result:
            messagebox.showinfo('Tic Tac Toe', result)
            self.root.destroy()
        else:
            self.view.update(self.model.board)


if __name__ == '__main__':
    controller = TicTacToeController()
