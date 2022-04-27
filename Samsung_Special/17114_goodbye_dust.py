'''
공기청정기 설치

1. 공기청정기 항상 1번 열: 크기 2행
2. 미세먼지의 확산
    2-1) r,c에 있는 먼지가 네 방향으로 확산
    2-2) 인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로 확산하지 않음
    2-3) 확산되는 양은 A_rc / 5, 소수점 강퇴
    2-4) 미세먼지 남은 양은 A_rc - (A_rc / 5) * 확산된 방향 개수
3. 공기청정기 바람
    3-1) 위쪽은 반 시계 방향으로 순환, 아래쪽은 시계방향으로 순환
    3-2) 모두 한칸씩 미세먼지가 이동
    3-3) 공기청정기로 이동하면 공기가 정화된다.

'''


R, C, T = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(R)]
cond = []
for r in range(R):
    if graph[r][0] == -1:
        cond.append(r)
up, down = cond

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def diffuse(g):
    to_diffuse = []
    for r in range(R):
        for c in range(C):
            air = g[r][c]
            if air and air != -1:
                cnt = 0
                for i in range(4):
                    moved_row = r + dx[i]
                    moved_col = c + dy[i]

                    if 0 <= moved_row < R and 0 <= moved_col < C and g[moved_row][moved_col] != -1:

                        to_diffuse.append([moved_row, moved_col, air//5])
                        cnt += 1
        
                to_diffuse.append([r, c,  -((air // 5) * cnt)])

    for row, col, airload in to_diffuse:
        g[row][col] += airload
    
    return g

# 공기 청정기의 방향은 정해져있지!
def condition_up(g, machine_loc):
    dx = [0,-1,0,1]
    dy = [1,0,-1,0]

    direction = 0

    cur_x, cur_y = machine_loc, 0
    temp = 0

    while True:
        moved_x = cur_x + dx[direction]
        moved_y = cur_y + dy[direction]

        if moved_x == machine_loc and moved_y == 0:
            break

        if 0 <= moved_x < R and 0 <= moved_y < C and g[moved_x][moved_y] != -1:
            g[moved_x][moved_y], temp = temp, g[moved_x][moved_y]
            cur_x, cur_y = moved_x, moved_y
        
        else:
            direction += 1

    return g

def condition_down(g, machine_loc):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    direction = 0
    cur_x, cur_y = machine_loc, 0

    temp = 0

    while True:
        moved_x = cur_x + dx[direction]
        moved_y = cur_y + dy[direction]

        if moved_x == machine_loc and moved_y == 0:
            break

        if 0 <= moved_x < R and 0 <= moved_y < C and g[moved_x][moved_y] != -1:
            g[moved_x][moved_y], temp = temp, g[moved_x][moved_y]
            cur_x, cur_y = moved_x, moved_y
        
        else:
            direction += 1

    return g

while T > 0:

    graph = diffuse(graph)
    graph = condition_up(graph, up)
    graph = condition_down(graph, down)

    T -= 1

total = 0
for r in range(R):
    for c in range(C):
        value = graph[r][c]
        if value != -1:
            total += value

print(total)