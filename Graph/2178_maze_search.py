N, M = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(N)]
count = [list(0 for _ in range(M)) for _ in range(N)]

# import sys
# input = sys.stdin.readline
from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(y: int, x: int) -> None:
    queue = deque()
    queue.append((y,x))
    count[y][x] = 1
    
    while queue:
        y,x = queue.popleft()
        for idx in range(4):
            y_axis = y+dy[idx]
            x_axis = x+dx[idx]
            if 0<=y_axis<N and 0<=x_axis<M:
                if graph[y_axis][x_axis] == 1:
                    if not count[y_axis][x_axis]:
                        count[y_axis][x_axis] = count[y][x] + 1
                        queue.append((y_axis, x_axis))
#                     elif count[y_axis][x_axis]:
#                         count[y_axis][x_axis] = min(count[y_axis][x_axis],count[y][x] + 1)
bfs(0,0)
print(count[-1][-1])