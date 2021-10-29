
grid = []


def gridInit():
    for x in range(3):
        r = []
        for y in range(3):
            r.append(' ')
        grid.append(r)


gridInit()


def display_board():
    print(
        f'''
TIC TAC TOE
*****************
*   {grid[0][0]} | {grid[0][1]} | {grid[0][2]}   *
*  ---|---|---  *
*   {grid[1][0]} | {grid[1][1]} | {grid[1][2]}   *
*  ---|---|---  *
*   {grid[2][0]} | {grid[2][1]} | {grid[2][2]}   *
*****************
'''
    )


print('Welcome to TIC TAC TOE!')
display_board()

# check if all grid was filled
def isGridFilled():
    for row in grid:
        for val in row:
            if val == ' ':
                return False
    print('It\'s a tie !')
    return True


def move(player, val):
    # verify we have 2 char
    if len(player) != 2:
        print('invalid value')
        return False

    x = player[0]
    y = player[1]

    # verify char are numeric
    if not (x+y).isnumeric():
        print('invalid value')
        return False

    x = int(x)
    y = int(y)

    # verify in range
    if 3 < x < 0 or 3 > y < 0:
        print('invalid value')
        return False

    # check if position occupied
    if grid[x][y] != ' ':
        print('position already occupied')
        return False

    # mark on grid
    grid[x][y] = val
    display_board()
    return True


def checkRows(v):
    for row in grid:
        if grid[0] == grid[1] == grid[2] == v:
            return True
    return False


def checkCols(v):
    for x in range(len(grid)):
        if grid[0][x] == grid[1][x] == grid[2][x] == v:
            return True
    return False


def checkDiagonals(v):
    return v == grid[0][0] == grid[1][1] == grid[2][2] or v == grid[2][0] == grid[1][1] == grid[0][2]


def check_win(v):
    return checkRows(v) or checkCols(v) or checkDiagonals(v)


while True:
    player1 = (input('player X please enter position(#row #column):\n')).split(' ')

    while not move(player1, 'X'):
        player1 = (input('player X try again:\n')).split(' ')

    if isGridFilled():
        break

    if check_win('X'):
        print('player X won !!!')
        break

    player2 = (input('player O please enter position(#row #column):\n')).split(' ')

    while not move(player2, 'O'):
        player2 = (input('position occupied, player O try again:\n')).split(' ')

    if isGridFilled():
        break
