from collections import defaultdict
'''
문제 description
1. 상어에 M개의 숫자
2. 냄새는 k턴동안 남고, 1의 번호를 가진 상어는 모두를 쫓아낼 수 있다.
3. 1초마다 상하좌우 인접 칸 이동 / 자신의 냄새 뿌린다.
4. 냄새는 상어가 k번 이동하면 사라진다 (유통기한)
5. 이동의 기준
    5-1) 인접 칸 아무 냄새 없는 칸의 방향
    5-2) 자신의 냄새가 있는 칸의 방향
    5-3) 우선순위 다르다.

각 상어의 방향이 차례대로 주어진다. 1, 2, 3, 4는 각각 위, 아래, 왼쪽, 오른쪽을 의미한다.

'''
dx = [-1,1,0,0]
dy = [0,0,-1,1]


def move_shark(graph, smell_graph, priority):
    N = len(graph)
    moved_shark = []
    for row_idx in range(N):
        for col_idx in range(N):
            # cell_idx, cell_dir = graph[row_idx][col_idx]
            # print(row_idx, col_idx)
            if graph[row_idx][col_idx] == []:
                continue

            # 상어가 해당 인덱스에 존재한다면,

            else:
                cell_idx, cell_dir = graph[row_idx][col_idx][0]

                if cell_idx in moved_shark:
                    continue
                else:
                    move_flag = 0
                    prior = priority[cell_idx][cell_dir]
                    for direction in prior:
                        moved_x = row_idx + dx[direction]
                        moved_y = col_idx + dy[direction]

                        # 격자 내에 들어오고 smell이 없다면
                        if 0 <= moved_x < N and 0 <= moved_y < N and smell_graph[moved_x][moved_y][1] == 0:
                            cell_num, _ = graph[row_idx][col_idx].pop()
                            graph[moved_x][moved_y].append([cell_num, direction])
                            moved_shark.append(cell_num)
                            move_flag = 1
                            break

                    if not move_flag:
                        for direction in prior:
                            moved_x = row_idx + dx[direction]
                            moved_y = col_idx + dy[direction]

                            if 0 <= moved_x < N and 0 <= moved_y < N and smell_graph[moved_x][moved_y][0] == cell_idx:
                                cell_num, _ = graph[row_idx][col_idx].pop()
                                graph[moved_x][moved_y].append([cell_num, direction])
                                moved_shark.append(cell_num)
                                move_flag = 1
                                break

    return graph, smell_graph

def competition_shark(graph):
    N = len(graph)
    for row_idx in range(N):
        for col_idx in range(N):
            cell = graph[row_idx][col_idx]
            if len(cell) > 1:
                min_id = min(cell, key = lambda x: x[0])[0]
                graph[row_idx][col_idx] = [i for i in cell if i[0] == min_id]
            else:
                pass
    return graph

def smell_control(graph, smell_graph, k):
    N = len(smell_graph)

    for row_idx in range(N):
        for col_idx in range(N):
            cell = graph[row_idx][col_idx]
            # 새로 냄새를 뿌리는 과정
            if len(cell) > 0:
                cell_idx, cell_dir = cell[0]
                smell_graph[row_idx][col_idx] = [cell_idx, k]
            
            else:
                smell_target = smell_graph[row_idx][col_idx]
                if smell_target[1] > 0:
                    smell_graph[row_idx][col_idx][1] -= 1

    return smell_graph

def check_final(graph):
    len_cell = 0
    for row_idx in range(N):
        for col_idx in range(N):
            cell = graph[row_idx][col_idx]
            if len(cell) > 0:
                len_cell += 1
            else:
                pass
    return len_cell

if __name__ == '__main__':
    # N, M, k = 격자 크기 / M 마리 상어 / k 냄새 잔류 기간
    N, M, k = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]

    smell_graph = [[0 for _ in range(N)] for _ in range(N)]

    shark_dir = list(map(int, input().split()))
    shark_dir = [i-1 for i in shark_dir]

    # 상어 위치 파악
    shark_loc = []
    for row_idx in range(N):
        for col_idx in range(N):
            if graph[row_idx][col_idx] != 0:
                shark_loc.append([row_idx, col_idx])

    # graph 에는 상어의 idx와 방향
    # smell 에는 상어의 idx와 유통기한
    for row_idx in range(N):
        for col_idx in range(N):
            current_value = graph[row_idx][col_idx]
            if current_value == 0:
                graph[row_idx][col_idx] = []
                smell_graph[row_idx][col_idx] = [0,0]
            else:
                graph[row_idx][col_idx] = [[current_value-1, shark_dir[current_value-1]]]
                smell_graph[row_idx][col_idx] = [current_value-1, k]
    

    priority = defaultdict(lambda: [])
    for i in range(M):
        for _ in range(4):
            directions = list(map(int, input().split()))
            priority[i].append([d-1 for d in directions])

    time = 0

    while True:
        
        graph, smell_graph = move_shark(graph, smell_graph, priority)
        graph = competition_shark(graph)
        smell_graph = smell_control(graph, smell_graph, k)
        len_cell = check_final(graph)
        time += 1
        if len_cell == 1:
            break
        if time == 1000:
            time = -1
            break
        # if time == 20:
        #     break
    print(time)


    

