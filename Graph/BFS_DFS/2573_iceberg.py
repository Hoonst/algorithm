from collections import deque, defaultdict
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def melt(graph):
    N, M = len(graph), len(graph[0])
    to_melt = []
    for row_idx in range(N):
        for col_idx in range(M):
            if graph[row_idx][col_idx] > 0:
                nearby = 0
                for i in range(4):
                    moved_row = row_idx + dx[i]
                    moved_col = col_idx + dy[i]
                    if 0 <= moved_row < N and 0 <= moved_col < M and graph[moved_row][moved_col] == 0:
                        nearby += 1

                to_melt.append([row_idx, col_idx, nearby])    

    for r,c,n in to_melt:
        graph[r][c] = graph[r][c] - n if graph[r][c] - n > 0 else 0

    return graph

def bfs(graph, row, col, visited):
    N, M = len(graph), len(graph[0])
    visited[row][col] = 1
    queue = deque()
    queue.append([row, col])

    while queue:
        row, col = queue.popleft()
        
        for i in range(4):
            moved_row = row + dx[i]
            moved_col = col + dy[i]

            if 0 <= moved_row < N and 0 <= moved_col < M and graph[moved_row][moved_col] != 0 and not visited[moved_row][moved_col]:
                queue.append([moved_row, moved_col])
                visited[moved_row][moved_col] = 1

    return 1, visited
                
def count_island(graph):
    N, M = len(graph), len(graph[0])
    visited = [[0 for _ in range(M)] for _ in range(N)]
    islands = 0
    for row_idx in range(N):
        for col_idx in range(M):
            if graph[row_idx][col_idx] > 0 and not visited[row_idx][col_idx]:
                island, visited = bfs(graph, row_idx, col_idx, visited)
                islands += island

    return islands

if __name__=='__main__':
    N, M = map(int, input().split())

    graph = [list(map(int, input().split())) for _ in range(N)]

    islands = 0
    year = 0

    while True:
        graph = melt(graph)
        islands = count_island(graph)
        year += 1

        if islands == 0:
            print(0)
            break
        
        if islands > 1:
            print(year)
            break 