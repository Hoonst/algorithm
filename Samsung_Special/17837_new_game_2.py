'''
새로운 게임 2
1. N x N / K개의 말 - 하나의 말 위에 다른 말을 올릴 수 있따.
2. 체스판은 흰색 / 빨간색 / 파란색
3. 말 K개를 올리고 시작, 이동방향도 정해져 있다.
4. 턴 한 번은 1번 말부터 K번 말까지 순서대로 이동
    1) 한 말이 이동할 떄 위에 있는 녀석도 함께 이동
    2) 말이 4개 이상 쌓이면 게임 종료
5. A번 말이 이동하려는 칸이
    1) 흰색이 경우 이동. 칸에 말이 이미 있는 경우, 가장 위에 얹는다
        1) A번 말의 위에 다른 말이 있는 경우 함께 이동
    2) 빨간색인 경우, 모든 말의 순서 반대 (이동하는 말만, 기존 말은 유지)
    3) 파란색인 경우, A번 말의 이동 방향 반대 (파란색에는 이동하지 않는다.)

'''
from collections import deque, OrderedDict
N, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

checks = [list(map(int, input().split())) for _ in range(K)]

checks_graph = [[[] for _ in range(N)] for _ in range(N)]

for idx, (x, y, direction) in enumerate(checks):
    checks_graph[x-1][y-1].append([idx, direction-1])

checks = {idx: [x-1,y-1,direction-1] for idx, (x,y,direction) in enumerate(checks)}
checks = OrderedDict(checks)

dx = [0,0,-1,1]
dy = [1,-1,0,0]


def move_check(graph, c_graph, check_idx):
    row, col, dir = checks[check_idx]

    moved_row = row + dx[dir]
    moved_col = col + dy[dir]

    def move(row, col, moved_row, moved_col, original_dir, changed_dir):
        c_index = c_graph[row][col].index([check_idx, original_dir])
        c_graph[row][col][c_index][1] = changed_dir
        move_target = c_graph[row][col][c_index:]

        # 빨간색과 
        if graph[moved_row][moved_col] == 1:
            move_target.reverse()
        
        # 체커보드 추가
        for t in move_target:
            c_graph[moved_row][moved_col].append(t)
        c_graph[row][col] = c_graph[row][col][:c_index]

        # 체커 정보 변경
        
        for check_temp, _ in move_target:
            _, _, dir = checks[check_temp]
            print(dir)
            checks[check_temp] = [moved_row, moved_col, changed_dir]

    if 0 <= moved_row < N and 0 <= moved_col < N:
        # 파란색 칸
        if graph[moved_row][moved_col] == 2:
            # 방향 전환
            if dir % 2 == 0:
                changed_dir = dir + 1
            else:
                changed_dir = dir - 1
            moved_row = row + dx[changed_dir]
            moved_col = col + dy[changed_dir]

            if 0 <= moved_row < N and 0 <= moved_col < N and graph[moved_row][moved_col] != 2:
                move(row, col, moved_row, moved_col, dir, changed_dir)
            else:
                checks[check_idx] = [row, col, changed_dir]


        else:
            # check index 보다 위에 있는 녀석들만 도려내야 한다.
            move(row, col, moved_row, moved_col, dir, dir)
    
    else:
        if dir % 2 == 0:
            changed_dir = dir + 1
        else:
            changed_dir = dir - 1
        moved_row = row + dx[changed_dir]
        moved_col = col + dy[changed_dir]
        if graph[moved_row][moved_col] != 2:
            move(row, col, moved_row, moved_col, dir, changed_dir)
        else:
            checks[check_idx] = [row, col, changed_dir]
        # 파란색과 동일한 절차


def process(graph, c_graph, check_infos):
    flag = 1
    turn = 0
    while flag:
        for check_idx in check_infos:
            print(f'check_idx: {check_idx}')
            move_check(graph, c_graph, check_idx)

        for i in range(N):
            for j in range(N):
                if len(c_graph[i][j]) == 4:
                    flag = 0

        turn += 1

        if turn == 1000:
            turn = -1
            break
    
    print(turn)


process(graph, checks_graph, checks)