from collections import deque
from copy import deepcopy

N, M, K = map(int, input().split())

fireballs = [list(map(int, input().split())) for _ in range(M)]
fireballs = [[r-1, c-1, m, s, d] for r,c,m,s,d in fireballs]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

graph = [[deque() for _ in range(N)] for _ in range(N)]
for fireball in fireballs:
    row, col, mass, speed, dir = fireball
    graph[row][col].append([mass, speed, dir])

def move_fireball(g):
    cands = []
    for i in range(N):
        for j in range(N):
            if g[i][j]:
                target = deepcopy(g[i][j])
                for m,s,d in target:
                    moved_row = (i + (dx[d] * s)) % N
                    moved_col = (j + (dy[d] * s)) % N

                    m,s,d = g[i][j].popleft()
                    cands.append([moved_row, moved_col, m,s,d])

    for r,c,m,s,d in cands:
        g[r][c].append([m,s,d])    

    return g

direction_list = [[0,2,4,6], [1,3,5,7]]

def after_move(g):
    for i in range(N):
        for j in range(N):
            if len(g[i][j]) > 1:
                target = deepcopy(g[i][j])
                balls = len(target)
                combined_mass = sum([m for m,_,_ in target]) // 5
                if combined_mass == 0:
                    g[i][j] = deque()
                    continue
                combined_speed = sum([s for _,s,_ in target]) // balls
                
                first_speed = target[0][2] % 2

                flag = 0
                for _, _, d in target:
                    if d % 2 != first_speed:
                        flag = 1

                g[i][j] = deque([combined_mass, combined_speed, d] for d in direction_list[flag])

    return g

for _ in range(K):
    graph = move_fireball(graph)
    graph = after_move(graph)

total_sum = 0
for i in range(N):
    for j in range(N):
        for k in range(len(graph[i][j])):
            total_sum += graph[i][j][k][0]

print(total_sum)