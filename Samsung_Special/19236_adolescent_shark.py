import copy

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

def fish_location(fish_id_graph):
    fish_dic = {}
    N = len(fish_id_graph)
    for row_idx in range(N):
        for col_idx in range(N):
            if fish_id_graph[row_idx][col_idx] > 0:
                fish_dic[fish_id_graph[row_idx][col_idx]] = [row_idx, col_idx]
    # 현재 fish들의 location 기록
    return dict(sorted(fish_dic.items()))

def shark_location(fish_id_graph):
    N = len(fish_id_graph)
    for row_idx in range(N):
        for col_idx in range(N):
            if fish_id_graph[row_idx][col_idx] == -1:
                return [row_idx, col_idx]

def move_fish(fish_id_graph, fish_direction_graph):
    target = 1
    N = len(fish_id_graph)

    fish_locs = fish_location(fish_id_graph)
    print(fish_locs)

    for fish_id in fish_locs:
        fish_loc = fish_locs[fish_id]
        fish_loc_row, fish_loc_col = fish_loc
        fish_direction = fish_direction_graph[fish_loc_row][fish_loc_col]

        trial = 8
        while trial:
            moved_row = fish_loc_row + dx[fish_direction % 8]
            moved_col = fish_loc_col + dy[fish_direction % 8]

            # 갈 수 있는 곳: 격자 내, 상어가 없는 칸, 물고기가 있는 칸

            # 방향과 위치를 바꿈
            if 0 <= moved_row < N and 0 <= moved_col < N and fish_id_graph[moved_row][moved_col] > 0:
                value_id = fish_id_graph[moved_row][moved_col]
                value_dir = fish_direction_graph[moved_row][moved_col]

                # swap을 해야 더 깔끔한 전략
                fish_id_graph[moved_row][moved_col] = fish_id_graph[fish_loc_row][fish_loc_col]
                fish_direction_graph[moved_row][moved_col] = fish_direction_graph[fish_loc_row][fish_loc_col]

                fish_locs[fish_id_graph[fish_loc_row][fish_loc_col]] = [moved_row, moved_col]

                fish_id_graph[fish_loc_row][fish_loc_col] = value_id
                fish_direction_graph[fish_loc_row][fish_loc_col] = value_dir

                fish_locs[value_id] = [fish_loc_row, fish_loc_col]
                break
            else:
                fish_direction += 1
                trial -= 1
        print(f'fish_id_graph: {fish_id_graph}')
        print(f'fish_direction_graph: {fish_direction_graph}')
    return fish_id_graph, fish_direction_graph

def food(array, directions, x, y):
    N = len(array)
    direction = directions[x][y]
    positions = []

    for _ in range(4):
        moved_x = x + dx[direction]
        moved_y = y + dy[direction]
        if 0 <= moved_x < N and 0 <= moved_y < N and array[moved_x][moved_y] != -2:
            positions.append([moved_x, moved_y])
        x, y = moved_x, moved_y
    return positions

def dfs(array, directions, x, y, total):
    global answer
    array = copy.deepcopy(array)

    shark_loc = shark_location(array)
    shark_row, shark_col = shark_loc

    # x,y 자리에 있는 물고기 먹기
    number = array[x][y]
    array[x][y] = -1

    # 상어의 원래 위치는 삭제
    array[shark_row][shark_col] = -2
    directions[shark_row][shark_col] = -1

    food_candidate = food(array, directions, x, y)

    answer = max(answer, total + number)

    for next_x, next_y in food_candidate:
        dfs(array, next_x, next_y, total + number)

if __name__ == '__main__':
    fish_info = [list(map(int, input().split())) for _ in range(4)]

    fish_id_graph = [[0 for _ in range(4)] for _ in range(4)]
    fish_direction_graph = [[0 for _ in range(4)] for _ in range(4)]

    for idx, row in enumerate(fish_info):
        ids = [row[i] for i in range(0,len(row),2)]
        dirs = [row[i]-1 for i in range(1, len(row)+1, 2)]

        fish_id_graph[idx] = ids
        fish_direction_graph[idx] = dirs

    print(fish_id_graph)
    print(fish_direction_graph)

    fish_id_graph[0][0] = -1

    fish_id_graph, fish_direction_graph = move_fish(fish_id_graph, fish_direction_graph)

    answer = 0

            
# dfs는 여러가지 경우의 수의 정답을 겹치는 것
# dfs는 탐색