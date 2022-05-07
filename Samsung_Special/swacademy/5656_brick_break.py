from collections import deque
from copy import deepcopy

# T = int(input())
N, W, H = map(int, input().split())
original_grid = [list(map(int, input().split())) for _ in range(H)]

answer = []
bizz = list(range(W))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def rotate90(g):
    g = list(zip(*g))
    g = [list(i[::-1]) for i in g]
    return g

original_grid = rotate90(original_grid)

def gravity(g):
    for w in range(W):
        for h in range(1, H):
            if g[w][h] == 0:
                continue
            elif g[w][h] != 0 and g[w][h-1] == 0:
                for idx in range(h-1, -1, -1):
                    if g[w][idx] != 0:
                        g[w][idx+1] = g[w][h]
                        g[w][h] = 0
                        break
                    elif g[w][idx] == 0 and idx == 0:
                        g[w][idx] = g[w][h]
                        g[w][h] = 0
                        break

    print('gravity')
    return g

def brick_break(bizs, g):
    target_idx = -1
    # 90도 회전을 했으니, 오른쪽에서부터 내려와야 한다.
    for biz in bizs:
        for idx in range(H-1, -1, -1):
            if g[biz][idx] != 0:
                target_idx = idx
                break
        if target_idx == -1:
            continue
        cell_num = g[biz][target_idx]
        # g[biz][target_idx] = 0

        kill_list = []
        if cell_num > 1:
            # 1은 자기 자신
            # 2는 자기 자신과 한 칸, 즉 N-1만큼을 감소시켜야 한다.

            queue = deque()
            queue.append([biz, target_idx])
            visited = [[0 for _ in range(H)] for _ in range(W)]
            
            while queue:
                head = queue.popleft()
                head_w, head_h = head
                cell_num = g[head_w][head_h]

                kill_list.append([head_w, head_h])
                visited[head_w][head_h] = 1

                if cell_num == 1:
                    continue
                
                for size in range(1, cell_num):
                    for dir in range(4):
                        right_left = head_h + (dy[dir] * size)
                        up_down = head_w + (dx[dir] * size)

                        # 터지는 곳이 격자 안에 포함되어 있고, 해당 cell이 존재한다면
                        if 0 <= right_left < H and 0 <= up_down < W and g[up_down][right_left] and not visited[up_down][right_left]:
                            visited[up_down][right_left] = 1
                            queue.append([up_down, right_left])
                            kill_list.append([up_down, right_left])
            
        elif cell_num == 1:
            g[biz][target_idx] = 0

        for kill in kill_list:
            g[kill[0]][kill[1]] = 0
            
        g = gravity(g)

    left = 0
    for i in range(len(g)):
        for j in range(len(g[0])):
            if g[i][j] != 0:
                left += 1
    print(bizs)
    print(left)

    return g, left


min_score = 1e9      
def comb(idx, temp):
    global min_score
    if len(temp) == N:
        grid = deepcopy(original_grid)
        grid, left = brick_break(temp, grid)

        if left < min_score:
            min_score = left
        return
    
    for i in range(idx, W):
        comb(i, temp + [bizz[i]])

comb(0, [])
print(min_score)