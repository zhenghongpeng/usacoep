fin = open('tttt.in', 'r')
fout = open('tttt.out', 'w')
board = []
winners = []
for i in range(3):
    board.append(list(fin.readline().strip()))


def countwinnerX(board_map, w):
    count1 = 0
    winners = set()
    for x in range(3):
        if board_map[0][x] == board_map[1][x] == board_map[2][x]:
            if board_map[0][x] == w:
                return True
    for x in range(3):
        if board_map[x][0] == board_map[x][1] == board_map[x][2]:
            if board_map[x][0] == w:
                return True
    if board_map[0][0] == board_map[1][1] == board_map[2][2]:
        if board_map[0][0] == w:
            return True
    if board_map[0][2] == board_map[1][1] == board_map[2][0]:
        if board_map[0][2] == w:
            return True
    return False


players = []
for x in board[0]:
    players.append(x)
for x in board[1]:
    players.append(x)
for x in board[2]:
    players.append(x)
players = sorted(list(set(players)))
count1 = 0
for k in players:
    if countwinnerX(board, k):
        count1 += 1
fout.write(str(count1)+'\n')
count2 = 0
winner = set()
for k in players:
    for l in players:
        if players.index(k) != players.index(l):
            temporary = [['' for i in range(3)] for j in range(3)]
            for i in range(3):
                for j in range(3):
                    if board[i][j] == l:
                        temporary[i][j] = k
                    else:
                        temporary[i][j] = board[i][j]
            print(k, l, temporary, board)

            if (not countwinnerX(board, k)) and countwinnerX(temporary, k):
                print(k, l, temporary, board, "***")
                winner.add((min(k, l), max(k, l)))
fout.write(str(len(winner))+'\n')
