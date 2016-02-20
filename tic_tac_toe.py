
board = [
    ['x', ' ', 'x'],
    ['x', 'x', 'o'],
    ['x', 'x', ' ']
]


def print_board():
    print ' {} | {} | {} '.format(board[0][0], board[0][1], board[0][2])
    print '---|---|---'
    print ' {} | {} | {} '.format(board[1][0], board[1][1], board[1][2])
    print '---|---|---'
    print ' {} | {} | {} '.format(board[2][0], board[2][1], board[2][2])


def who_won_row():
    someone_won = False
    for row in range(0, 3):
        if board[row][0] == board[row][1] == board[row][2]:
            someone_won = True
            break

    print 'is there a winning row? ', someone_won


def did_any_column_win():
    someone_won = False
    for column in range(0, 3):
        if board[0][column] == board[1][column] == board[2][column]:
            someone_won = True
            break

    print 'is there a winning column? ', someone_won


def who_won_diagonal1():
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


def who_won_diagonal2():
    who_won = ' '
    if board[0][0] == board[1][1] == board[2][2]:
        who_won = board[0][0]
    elif board[0][2] == board[1][1] == board[2][0]:
        who_won = board[0][2]

    return who_won

print_board()

print '{} won.'.format( who_won_row())
print '{} is learning from {}'.format('safayar',who_won_diagonal2())