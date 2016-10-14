import board
import player


def main():
    # create the board based on player specifications
    print "The board will be an nxm grid."
    n = raw_input("Please choose n: ")
    m = raw_input("Please choose m: ")
    print "The winner is the first player to get k marks in a row"
    k = raw_input("Please choose k: ")

    ck_board = board.Board(int(n), int(m), int(k))

    print ck_board

    # get player info
    player1_type = raw_input("Player1 is a Computer or Human? (c/h) ")
    if player1_type == "h":
        name1 = raw_input("Player 1's name: ")
        symbol1 = raw_input("Player 1's symbol: ")
    else:
        name1 = "P1: Computer"
        symbol1 = "o"

    player2_type = raw_input("Player2 is a Computer or Human? (c/h) ")
    if player2_type == "h":
        name2 = raw_input("Player 2's name: ")
        symbol2 = raw_input("Player 2's symbol: ")
        while symbol1 == symbol2:
            symbol2 = raw_input("Use a different symbol from Player 1: ")
    else:
        name2 = "P2: Computer"
        symbol2 = "o"
        if symbol1 == symbol2:
            symbol2 = "x"

    # Create players as humans or computers
    if player1_type == "h":
        player1 = player.HumanPlayer(name1, symbol1)
    else:
        player1 = player.ComputerPlayer(name1, symbol1, symbol2, ck_board)

    if player2_type == "h":
        player2 = player.HumanPlayer(name2, symbol2)
    else:
        player2 = player.ComputerPlayer(name2, symbol2, symbol1, ck_board)

    # set playing order
    curr_player = player1
    next_player = player2

    # gameplay, players switch off turns until there is a winner or tie game
    while not ck_board.has_winner() and not ck_board.is_full():
        print ck_board
        move = curr_player.prompt_move()
        while not ck_board.accepts_move(move):
            move = curr_player.prompt_move()
        (curr_player, next_player) = (next_player, curr_player)

    print ck_board

    if ck_board.has_winner():
        print "{} wins!".format(next_player)
    else:
        print "It's a draw!"


if __name__ == "__main__":
    main()
