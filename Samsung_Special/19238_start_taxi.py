'''
1. 도착지에 데려다줄때마다 연료가 충전되고, 바닥나면 끝
2. M 명의 승객을 태우는 것이 목표
3. 현재 위치에서 가장 거리가 짧은 승객 
4. 여러명이면 행번호 / 열번호가 가장 작은 승객
5. 다 태우면 이동하면서 소모한 연료 양의 두배가 충전
6. 이동하는 중에 연료가 바닥나면 이동 실패
7. 승객을 목적지에 이동시킨 동시에 연료가 바닥나면 실패 x

지역변수와 전역변수에 대한 고려를 제대로 하면서 해야함
'''
from copy import deepcopy
from collections import deque

N, M, gas = map(int, input().split())

taxi_map = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if taxi_map[i][j] == 1:
            taxi_map[i][j] = -1

original_map = deepcopy(taxi_map)

row, col = map(int, input().split())
row, col = row-1, col-1

guests = [list(map(int, input().split())) for _ in range(M)]
guests = [[from_x-1, from_y-1, to_x-1, to_y-1] for from_x, from_y, to_x, to_y in guests]
guests.sort(key=lambda x: [x[0], x[1]])

guest_from = [[x,y] for x,y,_,_ in guests]
guest_to = [[x,y] for _, _, x,y in guests]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def find_guest(g):
    '''
    가장 가까운 손님을 찾습니다.
    '''
    taxi_map = deepcopy(g)
    taxi_row, taxi_col = row, col

    queue = deque()
    queue.append([taxi_row, taxi_col])
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[taxi_row][taxi_col] = 1

    while queue:
        head = queue.popleft()
        taxi_row, taxi_col = head

        for i in range(4):
            moved_row = taxi_row + dx[i]
            moved_col = taxi_col + dy[i]

            if 0 <= moved_row < N and 0 <= moved_col < N and taxi_map[moved_row][moved_col] != -1 and not visited[moved_row][moved_col]:
                taxi_map[moved_row][moved_col] = taxi_map[taxi_row][taxi_col] + 1
                visited[moved_row][moved_col] = 1
                
                queue.append([moved_row, moved_col])
    
    min_loc = 10e9
    min_guest = 0
    for guest_idx in range(len(guest_from)):
        dist = taxi_map[guest_from[guest_idx][0]][guest_from[guest_idx][1]] 
        if 0 < dist < min_loc:
            min_loc = dist
            min_guest = guest_idx

    return min_guest, taxi_map

def find_dest(g):
    taxi_map = deepcopy(g)
    taxi_row, taxi_col = row, col

    queue = deque()
    queue.append([taxi_row, taxi_col])
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[taxi_row][taxi_col] = 1

    while queue:
        head = queue.popleft()
        taxi_row, taxi_col = head

        for i in range(4):
            moved_row = taxi_row + dx[i]
            moved_col = taxi_col + dy[i]

            if 0 <= moved_row < N and 0 <= moved_col < N and taxi_map[moved_row][moved_col] != -1 and not visited[moved_row][moved_col]:
                taxi_map[moved_row][moved_col] = taxi_map[taxi_row][taxi_col] + 1
                visited[moved_row][moved_col] = 1
                
                queue.append([moved_row, moved_col])
    
    return taxi_map

def drive2from(target_idx, taxi_map, gas):
    from_x, from_y = guest_from.pop(target_idx)
    row, col = 0, 0
    # 목적지로 출발
    # gas가 가는 비용보다 많음
    cost = taxi_map[from_x][from_y]

    if cost == 0:
        gas =-1

    elif cost <= gas:
        row, col = from_x, from_y
        gas -= cost

    else:
        gas = -1

    return row, col, gas

def drive2to(target_idx, taxi_map, gas):
    to_x, to_y = guest_to.pop(target_idx)
    row, col = 0, 0
    cost = taxi_map[to_x][to_y]

    if cost <= gas:
        row, col = to_x, to_y
        gas -= cost
        gas += (cost * 2)

    else:
        gas = -1

    return row, col, gas

while guest_from:
    min_guest, taxi_map = find_guest(original_map)
    # if min_guest == -1:
    #     break
    row, col, gas = drive2from(min_guest, taxi_map, gas)
    if gas == -1:
        break
    taxi_map = find_dest(original_map)
    row, col, gas = drive2to(min_guest, taxi_map, gas)
    if gas == -1:
        break
print(gas)