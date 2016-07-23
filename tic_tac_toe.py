
board = [
    [' ', ' ', ' '],
    ['x', 'x', 'x'],
    [' ', ' ', ' ']
]


# In the coordinates 1, 2 for example, the 1 is the row it's in and the 2 is the column it's in.
# This works for all coordinates, not just this one.
# A row is a line with three spaces that can be filled with an x,o or 
# A row/column index is a single number that is always 0, 1 or 2. 
# If I want to print whats at column index 2 and row index 1 I will type in 
# print board[1][2]


def print_board():
    print ' {} | {} | {} '.format(board[0][0], board[0][1], board[0][2])
    print '---|---|---'
    print ' {} | {} | {} '.format(board[1][0], board[1][1], board[1][2])
    print '---|---|---'
    print ' {} | {} | {} '.format(board[2][0], board[2][1], board[2][2])


def print_board_values():
    for row_index in range(0, 3):
        for column_index in range(0, 3):
            print 'row index: {}'.format(row_index)
            print 'column index: {}'.format(column_index)
            print board[row_index][column_index]

# what is a for loop
# Its a loop that makes it go back from where the loop starts
# then after it reaches the end it goes back the beginning until it is
# Write what this does for homework.


def who_won_row():
    who_won = ' '
    for row_index in range(0, 3):  
        if board[row_index][0] == board[row_index][1] == board[row_index][2] != " ":
            who_won = board[row_index][0]
            break

    return who_won


def who_won_column():
    who_won = ' '
    for column_index in range(0, 3):
        if board[0][column_index] == board[1][column_index] == board[2][column_index] != " ":
            who_won = board[0][column_index]
            break

    return who_won

#    someone_won = False
#    for column_index in range(0, 3):
#        if board[0][column_index] == board[1][column_index] == board[2][column_index]:
#            someone_won = True
#            break

#    return someone_won


def who_won_diagonal():
    who_won = ' '
    if board[0][0] == board[1][1] == board[2][2]:
        who_won = board[0][0]
    elif board[0][2] == board[1][1] == board[2][0]:
        who_won = board[0][2]

    return who_won


def who_has_entire_board():
    entire_board = ' '
    if board[0][0] == board[0][1] == board[0][2] == board[1][0] == board[1][1] == board[1][2] == board[2][0] == board[2][1] == board[2][2]:
        entire_board = board[0][0]

    return entire_board

# Make this function check to see if anything has the entire board.


def who_has_entire_board2():
    for row_index in range(0, 3):
        for column_index in range(0, 3):
            if board[row_index][column_index] != 'x':
                return 'Not all x.'
    return 'They are all x.'


# Ask the user for the row index and the column index.
# Ask it in two different questions.
def game_loop():
    print_board()
    print 'who_won_row: {}'.format(who_won_row())
    print 'who_won_column: {}'.format(who_won_column())
    print 'who_won_diagonal: {}'.format(who_won_diagonal())
    print 'who_has_entire_board: {}'.format(who_has_entire_board2())
    print 'what are board values:'
    print_board_values()

#    print 'Enter your row/column index.'
    row_index = int(raw_input("Enter your row index.: "))
    print 'You typed row index.'
    print row_index

    column_index = int(raw_input("Enter column index.: "))
    print 'You typed column index.'
    print column_index

    print "The board at this location is "
    print board[row_index][column_index]
    board[row_index][column_index] = 'x'
    print_board()
    

def who_won_diagonal_old():
    who_won = ' '
    if board[0][0] == board[1][1] == board[2][2] == 'x':
        who_won = board[0][0]
        print 'X won. '
    elif board[0][0] == board[1][1] == board[2][2] == 'o':
        who_won = board[0][0]
        print 'O won. '
    elif board[0][2] == board[1][1] == board[2][0] == 'x':
        who_won = board[0][2]
        print 'X won. '
    elif board[0][2] == board[1][1] == board[2][0] == 'o':
        who_won = board[0][2]
        print 'O won'

    return who_won


game_loop()


#print '{} won.'.format( who_won_column())
# print '{} is learning from {}'.format('safayar',who_won_diagonal2())
