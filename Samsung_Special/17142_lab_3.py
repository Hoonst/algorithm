from copy import deepcopy
from collections import deque

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

# 바이러스의 위치 찾기
temp_virus = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            graph[i][j] = '-'
        elif graph[i][j] == 2:
            graph[i][j] = '*'
            temp_virus.append([i,j])
        elif graph[i][j] == 0:
            graph[i][j] = -1
        
current_virus = []

answer = 10e9

def bfs(g, cv):
    global answer
    queue = deque()

    visited = [[0 for _ in range(N)] for _ in range(N)]

    for v in cv:
        v_r, c_r = v
        visited[v_r][c_r] = 1
        queue.append(v)

    max_num = -1
    while queue:
        head_v = queue.popleft()
        v_row, v_col = head_v

        for i in range(4):
            flag = 1
            moved_row = v_row + dx[i]
            moved_col = v_col + dy[i]

            if 0 <= moved_row < N and 0 <= moved_col < N and not visited[moved_row][moved_col] and not g[moved_row][moved_col] == '-':
                if g[moved_row][moved_col] == -1:
                    g[moved_row][moved_col] = g[v_row][v_col] + 1

                elif graph[moved_row][moved_col] == '*':
                    for j in range(4):
                        moved_row_inside = moved_row + dx[j]
                        moved_col_inside = moved_col + dy[j]
                        if 0 <= moved_row_inside < N and 0 <= moved_col_inside < N and not visited[moved_row_inside][moved_col_inside] and not g[moved_row_inside][moved_col_inside] == '-':
                            flag = 1
                            g[moved_row][moved_col] = g[v_row][v_col] + 1
                        else:
                            flag = 0
                            g[moved_row][moved_col] = g[v_row][v_col]


                elif g[moved_row][moved_col] > 0:
                    g[moved_row][moved_col] = min(g[moved_row][moved_col], g[v_row][v_col] + 1)

                
                visited[moved_row][moved_col] = 1
                if flag:
                    queue.append([moved_row, moved_col])

                # max_num = max(max_num, g[moved_row][moved_col])
                
    stop_flag = 0
    for i in range(N):
        for j in range(N):
            if type(g[i][j]) == int:
                max_num = max(max_num, g[i][j])
                if g[i][j] == -1:
                    max_num = -1
                    stop_flag = 1
                    break
        if stop_flag:
            break

    if max_num > -1:
        answer = min(max_num, answer)
        
                
def dfs(current_virus):
    if len(current_virus) == M:
        g = deepcopy(graph)
        print(current_virus)
        bfs(g, current_virus)
        return
    
    for virus_loc in temp_virus:
        virus_row, virus_col = virus_loc
        if virus_loc not in current_virus:

            current_virus.append(virus_loc)
            graph[virus_row][virus_col] = 0

            dfs(current_virus)

            current_virus.remove(virus_loc)
            graph[virus_row][virus_col] = '*'

dfs(current_virus)

if answer == 10e9:
    print(-1)
else:
    print(answer)