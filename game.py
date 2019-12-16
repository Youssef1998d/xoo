def checkForWin(l):

    def verifRow(list):
        for i in range(0, 7, 3):
            if list[i]+list[i+1]+list[i+2]=="XXX" or list[i]+list[i+1]+list[i+2]=="OOO":
                return True
        return False

    def verifCol(list):
        for i in range(0,3):
            if list[i]+list[i+3]+list[i+6]=="XXX" or list[i]+list[i+3]+list[i+6]=="OOO":
                return True
        return False

    def verifDiag(list):
        if list[0]+list[4]+list[8]=="XXX" or list[0]+list[4]+list[8]=="OOO" or list[2]+list[4]+list[6]=="OOO" or list[2]+list[4]+list[6]=="XXX":
            return True
        return False

    return verifRow(l) or verifCol(l) or verifDiag(l)

def checkForTie(l):
    return "-" not in l and not checkForWin(l)

def display_Board(l):
    for i in range(0, 9, 3):
        print(l[i], "|", l[i+1], "|", l[i+2],"\n")

def update_board(p, l, pl):
    l[p] = pl
    return l

def flip_player(p):
    dic = {"O":"X", "X":"O"}
    return dic[p]

def first():
    current = (input("Choose the first player x/o : ")).upper()
    return current

def handle_player_turn(player, board, i=0):
    if i==0:
        return handle_player_turn(first(), board, 1)
    else :
        if checkForWin(board):
            print(flip_player(player), " Won !")
            return True
        elif checkForTie(board):
            print("Game is Tie !")
            return True
        else:
            pos = int(input("It's {}'s turn, Choose a position 1-9 : ".format(player)))-1
            board = update_board(pos, board, player)
            display_Board(board)
            return handle_player_turn(flip_player(player), board, 1)

def runGame():
    l = ["-" for v in range(9)]
    display_Board(l)
    handle_player_turn("", l)

runGame()