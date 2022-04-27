'''
문제 설명
1. 상하좌우 인접
2. 블록: 검은색 블록, 무지개블록, 일반 블록 = 일반 블록은 M가지 색상이 존재
3. 검은색 블록은 -1 / 무지개 블록은 0으로 표현

4. 블록 그룹: 연결된 블록 집합
    4-1) 그룹 : 일반 블록 적어도 하나 (모두 같은 색)
    4-2) 검은색 있으면 안되고, 무지개 블록은 얼마나 들어있어도 된다.
    4-3) 블록 개수는 2보다 크거나 같고, 연결되어 있어야 한다. 
    4-4) 기준 블록: 일반 블록 중 행의 번호 / 열의 번호가 가장 작은 블록

5. 오토 플레이 (블록 그룹이 존재할 때 동안)
    5-1) 크기가 가장 큰 블록 수색: 여러개면 무지개가 많은 블록, 기준 블록의 행 / 열이 가장 큰 것
    5-2) 1에서 찾은 블록 그룹의 모든 블록 제거 = 점수 획득
    5-3) 격자에 중력 작용
    5-4) 격자 90도 반시계 방향 회전
    5-5) 다시 중력
'''
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def rainbow_block(blocks):
    max_zero_block = 0
    rainbow = []
    for block in blocks:
        zero_block = len([i for i in block if i[-1] == 0])
        if zero_block > max_zero_block:
            max_zero_block = zero_block

    for block in blocks:
        if len([i for i in block if i[-1] == 0]) == max_zero_block:
            rainbow.append(block)
    
    return rainbow

def criterion_block(blocks):
    blocks = [sorted(block, key = lambda x: [-x[2], x[0],x[1]]) for block in blocks]
    
    final_block = sorted(blocks, key= lambda x: [-x[0][0], -x[0][1]])[0]

    return final_block

def find_block_group(graph):
    max_block_size = 0
    N = len(graph)

    max_block_groups = []
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for row_idx in range(N):
        for col_idx in range(N):
            if not visited[row_idx][col_idx]:
                cell_value = graph[row_idx][col_idx]
                
                block_group = []
                # 일반 블록일 경우
                if cell_value > 0:
                    block_group.append([row_idx, col_idx, cell_value])
                    queue = deque([(row_idx, col_idx)])
                    
                    visited[row_idx][col_idx] = 1

                    while queue:
                        row_idx_, col_idx_ = queue.popleft()
                        # 상하좌우 수색
                        for i in range(4):
                            moved_x = row_idx_ + dx[i]
                            moved_y = col_idx_ + dy[i]

                            if 0 <= moved_x < N and 0 <= moved_y < N and not visited[moved_x][moved_y] and (graph[moved_x][moved_y] == 0 or graph[moved_x][moved_y] == cell_value):
                                if [moved_x, moved_y, graph[moved_x][moved_y]] not in block_group:
                                    block_group.append([moved_x, moved_y, graph[moved_x][moved_y]])
                                    queue.append((moved_x, moved_y))
                                    if graph[moved_x][moved_y] != 0:
                                        visited[moved_x][moved_y] = 1
                                
                
                    if len(block_group) >= max_block_size:
                        max_block_groups.append(block_group)
                        max_block_size = len(block_group)
    
    filtered_max_block_groups = [i for i in max_block_groups if (len(i) == max_block_size and len(i) > 1)]

    if len(filtered_max_block_groups) > 1:
        max_rainbow_groups = rainbow_block(filtered_max_block_groups)
        if len(max_rainbow_groups) > 1:
            max_criterion = criterion_block(max_rainbow_groups)
            return max_criterion
        else:
            return max_rainbow_groups[0]

    elif len(filtered_max_block_groups) == 0:
        return []

    else:
        return filtered_max_block_groups[0]
    
    # max_block_groups가 return


def erase_group(group, graph):
    # group = group[0]
    for g in group:
        row, col, _ = g
        graph[row][col] = -2        
    
    point = len(group)**2

    return graph, point

def gravity(graph):
    N = len(graph)
    for col_idx in range(N):
        for row_idx in range(N-1, -1, -1):
            value = graph[row_idx][col_idx]
            if value > -1:
                temp_row = row_idx
                while True:
                    moved_row_idx = row_idx + 1
                    # 시점이 한 칸 내려오고 값이 -2 라면
                    if 0 <= moved_row_idx < N and graph[moved_row_idx][col_idx] == -2:
                        row_idx = moved_row_idx
                    else:
                        if temp_row != row_idx:
                            graph[row_idx][col_idx] = graph[temp_row][col_idx]
                            graph[temp_row][col_idx] = -2
                            break
                        else:
                            break
    return graph

def rotate90(graph):
    N = len(graph)
    new_graph = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        row = [j[i] for j in graph]
        new_graph[N-1-i] = row

    return new_graph
            
if __name__ == '__main__':
    N, M = map(int, input().split())

    graph = [list(map(int, input().split())) for _ in range(N)]

    total_point = 0
    while True:
        group = find_block_group(graph)
        if group:
            graph, point = erase_group(group, graph)
            total_point += point

            graph = gravity(graph)
            graph = rotate90(graph)
            graph = gravity(graph)
        else:
            print(total_point)
            break