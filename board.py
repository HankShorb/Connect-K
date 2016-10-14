class Board(object):

    def __init__(self, n, m, k):
        self.n = n
        self.m = m
        self.k = k
        self.board = [[None for i in xrange(n)] for j in xrange(m)]

    # puts a move into the board, returns True if successfull False otherwise
    def accepts_move(self, move):
        for i in xrange(self.n):
            curr = self.board[move[0]][i]
            if not curr:
                self.board[move[0]][i] = move[1]
                return True
        return False

    # returns True if the board is full False otherwise
    def is_full(self):
        for i in xrange(self.m):
            if not self.board[i][self.n - 1]:
                return False
        return True

    # check if there is a winner on the board
    def has_winner(self):
        return (self._v_win() or self._h_win()
            or self._dr_win() or self._ur_win())

    # check for a vertical win
    def _v_win(self):
        for i in xrange(self.m):
            if self._winner_in_dir(self._up, i, 0):
                return True
        return False

    # check for a horizontal win
    def _h_win(self):
        for j in xrange(self.n):
            if self._winner_in_dir(self._right, 0, j):
                return True
        return False

    # check for a diagonal down right win
    def _dr_win(self):
        for i in xrange(self.m):
            if self._winner_in_dir(self._down_right, i, self.n - 1):
                return True
        for j in xrange(self.n):
            if self._winner_in_dir(self._down_right, 0, j):
                return True

        return False

    # check for a diagonal up right win
    def _ur_win(self):
        for i in xrange(self.m):
            if self._winner_in_dir(self._up_right, i, 0):
                return True
        for j in xrange(self.n):
            if self._winner_in_dir(self._up_right, 0, j):
                return True

        return False

    def _winner_in_dir(self, dir, i, j):
        count = 0
        prev = None
        while i < self.m and j < self.n:
            curr = self.board[i][j]
            if curr != prev:
                count = 0
            if curr:
                count += 1
            if count == self.k:
                return True
            (i, j) = dir(i, j)
            prev = curr

    def _up(self, i, j):
        return (i, j + 1)

    def _right(self, i, j):
        return (i + 1, j)

    def _down_right(self, i, j):
        return (i + 1, j - 1)

    def _up_right(self, i, j):
        return (i + 1, j + 1)

    # returns a string meant to display the board in the terminal
    def __str__(self):
        s = ["\n"]
        for i in xrange(self.m):
            s.append(str(i))
        s.append("\n")
        for j in xrange(self.n):
            for i in xrange(self.m):
                if self.board[i][-1 - j]:
                    s.append(self.board[i][-1 - j])
                else:
                    s.append('.')
            s.append("\n")
        for i in xrange(self.m):
            s.append(str(i))
        s.append("\n")

        return " " + " ".join(s)
