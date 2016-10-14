from random import randint
import copy


class Player(object):

    def __init__(self, name, symbol):
        self.name_str = name
        self.symbol = symbol

    def prompt_move(self):
        return (0, self.symbol)

    # to string method
    def __str__(self):
        return "{0} ({1})".format(self.name_str, self.symbol)


class HumanPlayer(Player):

    # Make a move
    def prompt_move(self):
        print "{}'s move".format(self)
        col = raw_input("Col #:")
        return (int(col), self.symbol)


class ComputerPlayer(Player):

    def __init__(self, name, symbol, opp_symbol, board):
        Player.__init__(self, name, symbol)
        self.board = board
        self.opp_symbol = opp_symbol

    # Computer plays randomly unless it sees potential win or loss on
    # following turn
    def prompt_move(self):
        move = (randint(0, self.board.m - 1), self.symbol)
        # try all possible next moves using both player's symbols
        # First try all computer moves to see if possible win
        possible_win = False
        for i in xrange(self.board.m):
            future_board = copy.deepcopy(self.board)
            future_board.accepts_move((i, self.symbol))
            if future_board.has_winner():
                move = (i, self.symbol)
                break

        # Then try all human moves to see if possible loss
        if not possible_win:
            for i in xrange(self.board.m):
                future_board = copy.deepcopy(self.board)
                future_board.accepts_move((i, self.opp_symbol))
                if future_board.has_winner():
                    move = (i, self.symbol)
                    break

        print "{}'s move".format(self)
        print "Col #: {}".format(move[0])
        return move
