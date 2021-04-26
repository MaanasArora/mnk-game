class GameState:
    def __init__(self, m, n, k):
        self.state = []
        self.m = m
        self.n = n
        self.k = k

    def get_turn(self):
        return len(self.state)

    def winning_player(self):
        player1 = [x[1:] for x in self.state if x[0] == 1]
        player2 = [x[1:] for x in self.state if x[0] == 2]

        for indx, player in enumerate((player1, player2)):
            for move in player:
                for direct in ((1, 0), (0, 1), (1, 1), (-1, 1)):
                    winning_moves = [(move[0]+i*direct[0],
                                      move[1]+i*direct[1]) for
                                      i in range(self.k)]

                    if all(winning_move in player for
                           winning_move in winning_moves):
                           return indx

        return None

    def place(self, player, x, y):
        if x >= self.m or y >= self.n:
            raise Exception('place move: square beyond bounds')

        if (1, x, y) in self.state or (2, x, y) in self.state:
            raise Exception('place move: square occupied')

        self.state.append((player, x, y))

    def play(self, x, y):
        turn = self.get_turn()
        player = (turn % 2) + 1

        self.place(player, x, y)

    def display(self):
        board = [['-' for j in range(self.n)] for
                 i in range(self.m)]

        for move in self.state:
            board[move[1]][move[2]] = 'X' if move[0] == 1 else 'O'

        for row in board:
            print('|', end='')
            for square in row:
                print('', square, '|', end='')
            print('\n')
