from collections import deque

N = int(input())

graph = [list(input()) for _ in range(N)]

new_graph = [[0]*N for _ in range(N)]

for y_idx in range(N):
    for x_idx in range(N):
        if graph[y_idx][x_idx] == 'G':
            new_graph[y_idx][x_idx] = 'R'
        else:
            new_graph[y_idx][x_idx] = graph[y_idx][x_idx]
            
visited = [[False]*N for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
red, green, blue = 0, 0, 0

def bfs(y,x,color, graph):
    queue = deque()
    queue.append((y,x))
    visited[y][x] = True
 
    while queue:
        y,x = queue.popleft()
 
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= nx < N and 0 <= ny < N:
                if graph[ny][nx] == color and not visited[ny][nx]:    # each color check
                    visited[ny][nx] = True
                    queue.append((ny, nx))
    return 1

for y in range(N):
    for x in range(N):
        if graph[y][x] == 'R' and not visited[y][x]:
            red += bfs(y,x, 'R', graph)
        elif graph[y][x] == 'G' and not visited[y][x]:
            green += bfs(y,x,'G', graph)
        elif graph[y][x] == 'B' and not visited[y][x]:
            blue += bfs(y,x,'B', graph)
print(red+green+blue)

red, blue = 0, 0
visited = [[False]*N for _ in range(N)]

for y in range(N):
    for x in range(N):
        if new_graph[y][x] == 'R' and not visited[y][x]:
            red += bfs(y,x, 'R', new_graph)
        elif new_graph[y][x] == 'B' and not visited[y][x]:
            blue += bfs(y,x,'B', new_graph)
print(red+blue)