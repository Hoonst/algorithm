import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(y: int, x: int) -> None:
    queue = deque()
    queue.append((y,x))
    visited[y][x] = True
    
    while queue:
        y,x = queue.popleft()
        for idx in range(4):
            y_axis = y+dy[idx]
            x_axis = x+dx[idx]
            if 0<=y_axis<N and 0<=x_axis<M:
                if land[y_axis][x_axis] == 1 and not visited[y_axis][x_axis]:
                    visited[y_axis][x_axis] = True
                    queue.append((y_axis, x_axis))
                    
for _ in range(T):
    bug = 0
    M, N, K = map(int, input().split())

    land = [[0]*M for i in range(N)]
    # M: 가로 길이, N: 세로 길이
    # y부터 indexing을 해야한다.

    for _ in range(K):
        x,y = map(int, input().split())
        land[y][x] = 1
    visited = [[False] * M for _ in range(N)]
    
    for y in range(N):
        for x in range(M):
            if land[y][x] == 1 and not visited[y][x]:
                bfs(y,x)
                bug += 1
    print(bug)