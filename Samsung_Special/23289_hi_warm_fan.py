from collections import deque

R, C, K = map(int, input().split())
# R, C: Row / Column
# K = Lowest Temperature
# graph 내에 온풍기의 정보가 적혀있음
# 온풍기 방향: 1 = 오른쪽 / 2 = 왼쪽 / 3 = 위 / 4 = 아래
# 5는 온도를 조사해야하는 칸 / 0은 빈칸


# 벽의 정보는 walls에 포함

# wall: 1이면 오른쪽에 / 0이면 위에 벽이 존재
graph = [list(map(int, input().split())) for _ in range(R)]
fans_direction = [1,2,3,4]
fans = [[i,j] for i in range(R) for j in range(C) if graph[i][j] in fans_direction]
need_check = [[i,j] for i in range(R) for j in range(C) if graph[i][j] == 5]
W = int(input())
walls = [list(map(int, input().split())) for _ in range(W)]
walls = [[[a-1,b-1], [a-1, b]] if c else [[a-1,b-1],[a-2, b-1]] for a,b,c in walls]
'''
1. 모든 온풍기에서 바람이 나온다.
    1. 온풍기에 의해 증가한 온도의 합
2. 온도가 조절
    1. 온도가 높은 칸에서 낮은 칸으로 온도가 이동
    2. 높은 곳은 감소 / 낮은 곳은 상승
    3. [(두 칸의 온도 차이) / 4] 만큼 온도가 조절
3. 온도가 1이상인 가장 바깥쪽 칸의 온도가 1씩 감소
4. 초콜릿
5. (조사해야하는) 모든 칸의 온도가 K 이상이 되었을 때 테스트 중단
'''

dr = [0,0,-1,1]
dc = [1,-1,0,0]

def wind_blow(my_fans, blown_graph):
    for fan in my_fans:
        wind_graph_temp = [[0 for _ in range(C)] for _ in range(R)]
        visited = [[0 for _ in range(C)] for _ in range(R)]

        queue = deque()
        row, col = fan
        dir = graph[row][col]-1
        visited[row][col] = 1

        # 온풍기가 있는 칸과 바람이 나오는 방향에 있는 칸 사이에는 벽이 없다.

        one_move = [row + dr[dir], col + dc[dir]]
        wind_graph_temp[one_move[0]][one_move[1]] = 5
        blown_graph[one_move[0]][one_move[1]] += 5
        queue.append(one_move)

        while queue:
            current = queue.popleft()
            current_row, current_col = current
            # wind dispersion
            wind_can_go = wind_disperse(current, dir)

            for wind_row, wind_col in wind_can_go:
                if wind_graph_temp[current_row][current_col] > 0 and not visited[wind_row][wind_col]:
                    wind_graph_temp[wind_row][wind_col] += wind_graph_temp[current_row][current_col]-1
                    blown_graph[wind_row][wind_col] += wind_graph_temp[current_row][current_col]-1
                    visited[wind_row][wind_col] = 1
                    queue.append([wind_row, wind_col])

    return blown_graph

def wind_disperse(source, direction):
    left = [[[-1,0], [0,1]], [[1,0], [0,-1]], [[0,-1],[-1,0]],[[0,-1],[1,0]]]
    right = [[[1,0],[0,1]], [[-1,0],[0,-1]], [[0, 1],[-1,0]], [[0,1],[1,0]]]
    
    to_left, to_right = left[direction], right[direction]
    side = [to_left, to_right]
    can_go = []

    # 왼쪽 / 오른쪽
    for s in side:
        total_flag = 0
        # 중심점
        source_row, source_col = source

        # 이동 경로
        # 왼쪽 오른쪽 한번씩 점검
        for move_r, move_c in s:
            source_temp = [source_row, source_col]
            move_source_row, move_source_col = source_row + move_r, source_col + move_c
            moved = [move_source_row, move_source_col]
            
            # 한번의 움직임 체크
            # 이게 되면 다음 움직임도 해본다.
            flag = 0
            if 0 <= move_source_row < R and 0 <= move_source_col < C:
                for wall in walls:
                    if source_temp in wall and moved in wall:
                        break
                    else:
                        flag += 1
                if flag == len(walls):
                    source_row, source_col = move_source_row, move_source_col
                    total_flag += 1
                else:
                    break
                    
        if total_flag == 2:
            can_go.append(moved)
    
    source_row, source_col = source
    center_move_row, center_move_col = source_row + dr[direction], source_col + dc[direction]   
    center = [center_move_row, center_move_col]
    flag = 0
    if 0 <= center_move_row < R and 0 <= center_move_col < C:
        for wall in walls:
            if source in wall and center in wall:
                break
            else:
                flag += 1
        if flag == len(walls):
            can_go.append([center_move_row, center_move_col])

    return can_go

def control_temp(temp_map):
    temp = [[0 for _ in range(C)] for _ in range(R)]

    for r in range(R):
        for c in range(C):
            base = temp_map[r][c]
            source = [r,c]
            cnt = 0
            if base:
                for i in range(4):
                    move_r, move_c = r + dr[i], c + dc[i]
                    moved = [move_r, move_c]
                    
                    if 0 <= move_r < R and 0 <= move_c < C and base > temp_map[move_r][move_c]:
                        # 두 칸의 온도 차이 / 4
                        diff = int((base - temp_map[move_r][move_c]) // 4)
                        flag = 0
                        for wall in walls:
                            if source in wall and moved in wall:
                                break
                            else:
                                flag += 1
                        if flag == len(walls):
                            cnt += diff
                            temp[move_r][move_c] += diff
            temp[r][c] += (base - cnt)
    return temp

def rim_cut(temp_map):
    first_row = temp_map[0]
    last_row = temp_map[-1]

    temp_map[0] = [i-1 if i > 0 else 0 for i in first_row]
    temp_map[-1] = [j-1 if j > 0 else 0 for j in last_row]
    for idx in range(1, C-1):
        if temp_map[idx][0]:
            temp_map[idx][0] -= 1
        if temp_map[idx][-1]:
            temp_map[idx][-1] -= 1
    return temp_map

def check_area(temp_map, checks):
    for check in checks:
        check_row, check_col = check
        if temp_map[check_row][check_col] < K:
            return False
    return True


choco = 0
blown_graph = [[0 for _ in range(C)] for _ in range(R)]

while True:
    blowed = wind_blow(fans, blown_graph)
    controlled = control_temp(blowed)
    blown_graph = rim_cut(controlled)
    choco += 1
    area_check = check_area(blown_graph, need_check)
    if area_check:
        print(choco)
        break
    if choco > 100:
        print(101)
        break