import numpy as np

class Game:
    def __init__(self, m, n, k):
        self.board = np.zeros((m, n))
        self.m = m
        self.n = n
        self.k = k
    
    def get_turn(self):
        return np.count_nonzero(self.board)

    def get_player_moves(self, player):
        return np.where(self.board==player)

    def check_win(self):
        raise NotImplementedError

    def place(self, player, x, y):
        if x >= self.m or y >= self.n:
            raise Exception('place move: square beyond bounds')

        if self.board[x, y] != 0:
            raise Exception('place move: square occupied')

        self.board[x, y] = player

    def play(self, x, y):
        turn = self.get_turn()
        player = (turn % 2) + 1

        self.place(player, x, y)

    def display(self):
        raise NotImplementedError
