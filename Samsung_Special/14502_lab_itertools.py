from collections import deque
from itertools import combinations
import copy

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def infection_bfs(y,x):
    queue = deque()
    queue.append((y,x))
    visited[y][x] = True
    
    total = 1
    while queue:
        y,x = queue.popleft()
        for index in range(4):
            y_axis = y + dy[index]
            x_axis = x + dx[index]
            if 0 <= y_axis < N and 0 <= x_axis < M:
                if copied_map[y_axis][x_axis] == 0 and not visited[y_axis][x_axis]:
                    # visit mark
                    visited[y_axis][x_axis] = True
                    # infected
                    copied_map[y_axis][x_axis] = 2
                    queue.append((y_axis, x_axis))

N, M = map(int, input().split())
mmap = [list(map(int, input().split())) for _ in range(N)]

not_infected = [(i,j) for i in range(len(mmap)) for j in range(len(mmap[i])) if mmap[i][j] == 0]
not_infected_comb = combinations(not_infected, 3)

maxi = 0
for group in not_infected_comb:
    visited = [[0]*M for _ in range(N)]
    
    # 맵 복사
    copied_map = copy.deepcopy(mmap)
    
    # 벽 세우기
    for y_idx, x_idx in group:
        copied_map[y_idx][x_idx] = 1
    
    # 바이러스 위치에서부터 전염 진행
    for y in range(N):
        for x in range(M):
            if copied_map[y][x] == 2 and not visited[y][x]:
                infection_bfs(y,x)
    
    temp_maxi = 0
    for j in copied_map:
        sum_j = sum([1 for k in j if k == 0])
        temp_maxi += sum_j

    if temp_maxi > maxi:
        maxi = temp_maxi
print(maxi)