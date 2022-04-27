from collections import deque
from copy import deepcopy

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]



N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

answer = 0

def find_virus():
    virus = []
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 2:
                virus.append([i,j])
    return virus

def bfs(g):
    queue = deque()
    visited = [[0 for _ in range(M)] for _ in range(N)]
    virus = find_virus()
    for v in virus:
        queue.append(v)
        visited[v[0]][v[1]] = 1

    while queue:
        head = queue.popleft()
        row, col = head

        for i in range(4):
            moved_row = row + dx[i]
            moved_col = col + dy[i]

            if 0 <= moved_row < N and 0 <= moved_col < M and g[moved_row][moved_col] == 0:
                g[moved_row][moved_col] = 3
                visited[moved_row][moved_col] = 1
                queue.append([moved_row, moved_col])

    check_safety(g)

def check_safety(g):
    global answer
    
    cnt = 0
    for i in range(N):
        for j in range(M):
            if g[i][j] == 0:
                cnt += 1
    answer = max(answer, cnt)


def dfs(wall_cnt):
    if wall_cnt == 3:
        bfs(deepcopy(graph))
        return
    
    for n in range(N):
        for m in range(M):
            if graph[n][m] == 0:
                graph[n][m] = 1
                dfs(wall_cnt+1)
                graph[n][m] = 0

dfs(0)

print(answer)