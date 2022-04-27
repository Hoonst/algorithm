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

checks = [[x-1,y-1,direction-1] for x,y,direction in checks]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def direction_shift(direct):
    if direct % 2 == 0:
        direct += 1
    else:
        direct -= 1
    return direct

def move_horse(horse_num):
    row, col, dir = checks[horse_num]
    
    moved_row = row + dx[dir]
    moved_col = col + dy[dir]

    if 0 <= moved_row < N and 0 <= moved_col < N:
        if graph[moved_row][moved_col] == 0:
            for check_idx, (horse_idx, horse_dir) in enumerate(checks_graph[row][col]):
                if horse_idx == horse_num:
                    break

            to_move = checks_graph[row][col][check_idx:][:]
            checks_graph[row][col] = checks_graph[row][col][:check_idx]    

            for m in to_move:
                checks_graph[moved_row][moved_col].append(m)
                m_idx, m_dir = m
                checks[m_idx] = [moved_row, moved_col, m_dir]
        
        elif graph[moved_row][moved_col] == 1:
            for check_idx, (horse_idx, horse_dir) in enumerate(checks_graph[row][col]):
                if horse_idx == horse_num:
                    break

            # checks_graph move
            to_move = checks_graph[row][col][check_idx:][-1::-1]
            checks_graph[row][col] = checks_graph[row][col][:check_idx]    
            for m in to_move:
                checks_graph[moved_row][moved_col].append(m)
                m_idx, m_dir = m
                checks[m_idx] = [moved_row, moved_col, m_dir]

            # checks change
        elif graph[moved_row][moved_col] == 2:
            print(f'original: {dir}')
            dir = direction_shift(dir)
            print(f'changed: {dir}')

            print(f'horse_num: {horse_num}')

            moved_row = row + dx[dir]
            moved_col = col + dy[dir]
            print(f'checks before: {checks}')
            checks[horse_num][-1] = dir
            print(f'checks after: {checks}')

            if 0 <= moved_row < N and 0 <= moved_col < N:
                if graph[moved_row][moved_col] == 2:
                    for check_idx, (horse_idx, horse_dir) in enumerate(checks_graph[row][col]):
                        if horse_idx == horse_num:
                            break
                    
                    checks_graph[row][col][check_idx][1] = dir
                    checks[horse_num] = [row, col, dir]
                    # checks[horse_num][-1] = dir
                
                else:
                    if graph[moved_row][moved_col] == 0:
                        
                        for check_idx, (horse_idx, horse_dir) in enumerate(checks_graph[row][col]):
                            if horse_idx == horse_num:
                                break
                        to_move = checks_graph[row][col][check_idx:][:]

                        checks_graph[row][col] = checks_graph[row][col][:check_idx]    
                        for m in to_move:
                            checks_graph[moved_row][moved_col].append(m)
                            m_idx, m_dir = m
                            checks[m_idx] = [moved_row, moved_col, m_dir]                        
                    
                    elif graph[moved_row][moved_col] == 1:
                        for check_idx, (horse_idx, horse_dir) in enumerate(checks_graph[row][col]):
                            if horse_idx == horse_num:
                                break
                        to_move = checks_graph[row][col][check_idx:][-1::-1]
                        checks_graph[row][col] = checks_graph[row][col][:check_idx]    
                        for m in to_move:
                            checks_graph[moved_row][moved_col].append(m)
                            m_idx, m_dir = m
                            checks[m_idx] = [moved_row, moved_col, m_dir]

            else:
                for check_idx, (horse_idx, horse_dir) in enumerate(checks_graph[row][col]):
                    if horse_idx == horse_num:
                        break
                
                checks_graph[row][col][check_idx][1] = dir
                # checks[horse_num][-1] = dir

    else:
        dir = direction_shift(dir)

        moved_row = row + dx[dir]
        moved_col = col + dy[dir]

        checks[horse_num][-1] = dir

        if 0 <= moved_row < N and 0 <= moved_col < N:
            if graph[moved_row][moved_col] == 2:
                for check_idx, (horse_idx, horse_dir) in enumerate(checks_graph[row][col]):
                    if horse_idx == horse_num:
                        break
                
                checks_graph[row][col][check_idx][1] = dir
                # checks[horse_num][-1] = dir
            
            else:
                if graph[moved_row][moved_col] == 0:
                    
                    for check_idx, (horse_idx, horse_dir) in enumerate(checks_graph[row][col]):
                        if horse_idx == horse_num:
                            break
                    to_move = checks_graph[row][col][check_idx:][:]

                    checks_graph[row][col] = checks_graph[row][col][:check_idx]    
                    for m in to_move:
                        checks_graph[moved_row][moved_col].append(m)
                        m_idx, m_dir = m
                        checks[m_idx] = [moved_row, moved_col, m_dir]                        
                
                elif graph[moved_row][moved_col] == 1:
                    for check_idx, (horse_idx, horse_dir) in enumerate(checks_graph[row][col]):
                        if horse_idx == horse_num:
                            break
                    to_move = checks_graph[row][col][check_idx:][-1::-1]
                    checks_graph[row][col] = checks_graph[row][col][:check_idx]    
                    for m in to_move:
                        checks_graph[moved_row][moved_col].append(m)
                        m_idx, m_dir = m
                        checks[m_idx] = [moved_row, moved_col, m_dir]

        else:
            for check_idx, (horse_idx, horse_dir) in enumerate(checks_graph[row][col]):
                if horse_idx == horse_num:
                    break
            
            checks_graph[row][col][check_idx][1] = dir
            # checks[horse_num][-1] = dir



turn = 0
flag = 1
while flag:
    for k in range(K):
        move_horse(k)
    turn += 1

        # check the piles
    for i in range(N):
        for j in range(N):
            if len(checks_graph[i][j]) >= 4:
                flag = 0
                break

    if turn > 1000:
        turn = -1
        break
    
print(turn)


                    

