dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]

shark_dx = [-1, 0, 1, 0]
shark_dy = [0, -1, 0, 1]

def fish_move(fish_list):
    for fish in fish_list:
        fx, fy, d = fish

        cnt = 8
        while cnt:
            move_x = fx + dx[d % 8]
            move_y = fy + dy[d % 8]

            # 격자의 범위를 벗어나지 않는 칸
            if 0 <= move_x < 4 and 0 <= move_y < 4:
                # 물고기의 냄새가 없는 칸
                if graph[move_x][move_y] != 1:
                    # 상어가 없는 칸
                    if graph[move_x][move_y] ==:
                        graph[move_x][move_y] = (0,d)
            else:
                cnt -= 1
                d += 1

def shark_move(shark_loc):
    shark_x, shark_y = shark_loc





if __name__ == '__main__':
    M, S = map(int, input().split())
    fish_info = [list(map(int, input().split())) for _ in range(M)]
    fish_info = [[fx-1, fy-1, d] for fx, fy, d in fish_info]
    shark = list(map(int, input().split()))
    shark = [shark[0]-1, shark[1]-1]
    shark_x, shark_y = shark

    visited = [[0 for _ in range(4)] for _ in range(4)]
    smell = [[0 for _ in range(4)] for _ in range(4)]

    graph = [[0 for _ in range(4)] for _ in range(4)]
    for fish in fish_info:
        fx, fy, d = fish
        graph[fx][fy] = (0,d)
    
    graph[shark_x][shark_y] = (1, 0)
    



