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

