# https://chldkato.tistory.com/196?category=876515
from collections import deque

def dice_roll(dice, direction):
    if direction == 1 : # east
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3] 
    elif direction == 2: # west
        dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4] 
    elif direction == 3: # south
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2] 
    else:                # north
        dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]

    return dice

# 1. 주사위가 이동 방향으로 한 칸 굴러간다. 만약, 이동 방향에 칸이 없다면, 이동 방향을 반대로 한 다음 한 칸 굴러간다.
def rolling_stone(dice_loc, direction, graph):
    N, M = len(graph), len(graph[0])
    dr = [0,0,0,1,-1]
    dc = [0,1,-1,0,0]

    dice_row, dice_col = dice_loc
    move_dice_row, move_dice_col = dice_row + dr[direction], dice_col + dc[direction]
    if (move_dice_row < 0 or move_dice_row >= N) or (move_dice_col < 0 or move_dice_col >= M):
        direction = opposite_direction[direction]
        dice_row, dice_col = dice_loc
        move_dice_row, move_dice_col = dice_row + dr[direction], dice_col + dc[direction]

    return [move_dice_row, move_dice_col], direction

def get_point(dice_loc, graph):
    dr = [0,0,1,-1]
    dc = [1,-1,0,0]

    point = 1
    dice_row, dice_col = dice_loc
    value = graph[dice_row][dice_col]
    visited = [[0 for _ in range(M)] for _ in range(N)]

    queue = deque()
    queue.append([dice_row, dice_col])
    visited[dice_row][dice_col] = 1

    while queue:
        dice_row, dice_col = queue.popleft()

        for i in range(4):
            moved_row, moved_col = dice_row + dr[i], dice_col + dc[i]
            if 0 <= moved_row < N and 0 <= moved_col < M and not visited[moved_row][moved_col]:
                visited[moved_row][moved_col] = 1
                if graph[moved_row][moved_col] == value:
                    queue.append([moved_row, moved_col])
                    point += 1

    return point * value
                    
def select_direction(dice, dice_loc, direction, graph):
    dice_row, dice_col = dice_loc
    dice_bottom = dice[6]
    ground = graph[dice_row][dice_col]

    if dice_bottom > ground:
        direction = clockwise[direction]
    elif dice_bottom < ground:
        direction = counter_clockwise[direction]
    return direction

# 2. 주사위가 도착한 칸 (x, y)에 대한 점수를 획득한다.

# 3. 주사위의 아랫면에 있는 정수 A와 주사위가 있는 칸 (x, y)에 있는 정수 B를 비교해 이동 방향을 결정한다.


if __name__ == '__main__':
    N, M, K = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    dice_location = [0,0]
    dice_direction = 1

    opposite_direction = {1:2, 2:1, 3:4, 4:3}
    clockwise ={1:3, 3:2, 2:4, 4:1}
    counter_clockwise = {1:4, 4:2, 2:3, 3:1}
    dice = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6}
    point = 0
    for _ in range(K):
        # 한칸 구르기
        dice_location, dice_direction = rolling_stone(dice_location, dice_direction, graph)
        dice = dice_roll(dice, dice_direction)
        # 점수 얻기
        point += get_point(dice_location, graph)
        # 빙향 바꾸기
        dice_direction = select_direction(dice, dice_location, dice_direction, graph)
    print(point)
    


