row, col = 12, 6

graph = [list(input()) for _ in range(row)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

from collections import deque

def explosion(g):
    flag = 1
    answer = 0
    while True:
        start_floor = 0
        for floor in range(len(g)):
            if g[floor] != ['.','.','.','.','.','.']:
                start_floor = floor
                break
        g = g[start_floor:]

        N, M = len(g), len(g[0])
        visited = [[0 for _ in range(M)] for _ in range (N)]
        to_explode = []
        for n in range(N):
            for m in range(M):
                cell = g[n][m]
                if cell != '.':
                    temp_explode = []                    
                    queue = deque()
                    queue.append([n,m])
                    visited[n][m] = 1
                    temp_explode.append([n,m])

                    while queue:
                        head = queue.popleft()
                        x,y = head
                        for i in range(4):
                            moved_n = x + dx[i]
                            moved_m = y + dy[i]

                            if 0 <= moved_n < N and 0 <= moved_m < M and g[moved_n][moved_m] == cell and not visited[moved_n][moved_m]:
                                temp_explode.append([moved_n, moved_m])
                                visited[moved_n][moved_m] = 1
                                queue.append([moved_n, moved_m])

                    
                    if len(temp_explode) >= 4:
                        to_explode.append(temp_explode)
        
        if to_explode:
            for explode in to_explode:
                for ex_row, ex_col in explode:
                    g[ex_row][ex_col] = '.'
            answer += 1
            g = gravity(g)
            
        else:
            break
    return answer

def gravity(g):
    N, M = len(g), len(g[0])
    
    for col in range(M):
        for row in range(N-1,-1,-1):
            cell = g[row][col]
            if cell != '.':
                current_level = row
                
                while True:
                    next_level = current_level + 1
                    if next_level < N and g[next_level][col] == '.':
                        g[next_level][col] = g[current_level][col]
                        g[current_level][col] = '.'
                        current_level = next_level
                    else:
                        break
    return g

print(explosion(graph))