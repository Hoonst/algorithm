import copy
board = [[] for _ in range(4)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

for i in range(4):
    data = list(map(int, input().split()))
    fish = []
    for j in range(4):
        # 물고기 번호, 방향
        fish.append([data[2*j], data[2*j+1]-1])
    board[i] = fish

max_score = 0

def dfs(sx, sy, score, board):
    global max_score
    score += board[sx][sy][0]
    max_score = max(max_score, score)

    # shark index = 0
    board[sx][sy][0] = 0

    for fish_idx in range(1, 17):
        fish_x, fish_y = -1,-1

        for x in range(4):
            for y in range(4):
                if board[x][y][0] == fish_idx:
                    fish_x, fish_y = x, y
        # 물고기 못찾으면 다음 물고기 찾자
        if fish_x == -1 and fish_y == -1:
            continue

        fish_d = board[fish_x][fish_y][1]

        for i in range(8):
            nd = (fish_d+i)%8
            nx = fish_x + dx[nd]
            ny = fish_y + dy[nd]

            if not (0 <= nx < 4 and 0 <= ny < 4) or (nx == sx and ny == sy):
                continue
                
            board[fish_x][fish_y][1] = nd
            board[fish_x][fish_y], board[nx][ny] = board[nx][ny], board[fish_x][fish_y]
            break
        
        shark_d = board[sx][sy][1]
        for i in range(1, 5):
            nx = sx + dx[shark_d]*i
            ny = sy + dy[shark_d]*i
            if (0<= nx < 4 and 0<= ny < 4) and board[nx][ny][0] > 0:
                dfs(nx, ny, score, copy.deepcopy(board))


dfs(0, 0, 0, board)
print(max_score)
