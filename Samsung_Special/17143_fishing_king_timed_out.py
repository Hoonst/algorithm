'''
낚시왕

1. 칸에는 상어가 최대 한 마리 포함 (상어 크기 & 속도)
2. 1초에 일어나는 일
    1) 낚시왕이 오른쪽 한 칸 이동
    2) 낚시왕이 있는 열에 있는 상어 중에 땅과 가장 가까운 상어 잡기 / 상어를 잡으면 격자판에서 사라진다.
    3) 상어 이동
        1. 상어 이동 방식: 주어진 방향과 속도로 이동 / 격자를 넘는 경우는 방향을 반대로 바꾸어 속력 유지하여 이동
        2. 같은 칸에 상어가 두 마리 이상 존재 하면, 크기 큰 녀석이 작은 녀석을 잡아 먹어라!

모든 row / col을 도는 것은 현명하지 않은 선택인 것 같다.
선택적 row / col을 도는 것을 봐야 한다 > 시간 초과 발생
'''

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def process(graph, shark_info):
    seconds = len(graph[0])
    rows = len(graph)

    king_loc = 0
    total_weight = 0

    while king_loc < seconds:
        # 상어 사냥
        # 여기도 수정 필요 가능
        # for row_idx in range(rows):
        #     if graph[row_idx][king_loc]:
        #         speed, direction, weight = graph[row_idx][king_loc]
        #         total_weight += weight
        #         graph[row_idx][king_loc] = 0
                
        #         shark_info.remove([row_idx, king_loc, speed, direction, weight])
        #         break

        del_shark_info = [[r,c,s,d,w] for r,c,s,d,w in shark_info if c == king_loc]
        if del_shark_info:
            target_info = min(del_shark_info, key= lambda x: x[0])
            r,c,s,d,w = target_info
            total_weight += w
            graph[r][c] = 0
            shark_info.remove(target_info)
            

        # 상어 이동
        temp = []
        for row_idx, col_idx, speed, direction, weight in shark_info:

        # for row_idx in range(rows):
        #     original_row_idx = row_idx
        #     for col_idx in range(seconds):
        #         row_idx = original_row_idx
                # 상어가 존재한다면
            # speed, direction, weight = graph[row_idx][col_idx]
            graph[row_idx][col_idx] = 0
            original_speed = speed

            while speed:
                if direction < 2:
                    if 0 <= row_idx + dx[direction] < rows:
                        moved_x = row_idx + dx[direction]
                        row_idx = moved_x
                        speed -= 1
                    else:
                        direction = direction - 1 if direction % 2 == 1 else direction + 1
                        moved_x = row_idx + dx[direction]

                        row_idx = moved_x
                        speed -= 1

                elif direction >= 2:
                    if 0 <= col_idx + dy[direction] < seconds:
                        moved_y = col_idx + dy[direction]
                        col_idx = moved_y
                        speed -= 1
                    else:
                        direction = direction - 1 if direction % 2 == 1 else direction + 1
                        moved_y = col_idx + dy[direction]

                        col_idx = moved_y
                        speed -= 1
            
            temp.append([row_idx, col_idx, original_speed, direction, weight])

        new_shark_info = []
        new_graph = [[0 for _ in range(seconds)] for _ in range(rows)]
        temp = sorted(temp, key=lambda x: -x[-1])
        
        for r,c,s,d,w in temp:
            if new_graph[r][c]:
                current_speed, current_direction, current_weight = new_graph[r][c]
                if w > current_weight:
                    new_graph[r][c] = [s,d,w]
                    new_shark_info.append([r,c,s,d,w])
                
            else:
                new_graph[r][c] = [s,d,w]
                new_shark_info.append([r,c,s,d,w])

        graph = new_graph[:]
        shark_info = new_shark_info[:]
    
        king_loc += 1

    return total_weight
                            
if __name__ == '__main__':
    R, C, M = map(int, input().split())
    if M:
        shark_info = [list(map(int, input().split())) for _ in range(M)]
        shark_info = [[r-1,c-1,s,d-1,z] for r,c,s,d,z in shark_info]

        graph = [[0 for _ in range(C)] for _ in range(R)]

        for row, col, speed, direction, weight in shark_info:
            graph[row][col]=[speed, direction, weight]

        total_weight = process(graph, shark_info)
        print(total_weight)
    else:
        print(0)