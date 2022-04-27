'''
1. 2 0 1
2의 배 수인 원판을 d 방향으로 1칸 회전
2. 원판의 '인접하면서, 같은 수를 모두 지운다'
3. 없는 경우에는 원판에 적힌 수의 평균을 구하고 평균보다 큰 수에서 1을 빼고, 작은 수에는 1을 더한다.
'''

from collections import deque
import copy

N, M, T = map(int, input().split())
graph = [deque(map(int, input().split())) for _ in range(N)]

xdk = [list(map(int, input().split())) for _ in range(T)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def rotate(g, xx, dd, kk):
    if dd == 0:
        dd = 1
    elif dd == 1:
        dd = -1

    for row_idx in range(1, len(g)+1):
        if row_idx % xx == 0:
            g[row_idx-1].rotate(dd * kk)

    return g

def candidate(g):
    to_erase = []
    visited = [[0 for _ in range(M)] for _ in range(N)]
    to_erase = []
    for r in range(N):
        for c in range(M):
            cell = g[r][c]
            if cell > 0:
                queue = deque()
                queue.append([r,c])

                while queue:
                    head = queue.popleft()
                    head_row, head_col = head

                    for i in range(4):
                        moved_r = head_row + dx[i]
                        moved_c = head_col + dy[i]

                        if moved_c == -1:
                            moved_c = M-1
                        elif moved_c == M:
                            moved_c = 0

                        if 0 <= moved_r < N and 0 <= moved_c < M and g[moved_r][moved_c] == cell and not visited[moved_r][moved_c]:
                            queue.append([moved_r, moved_c])
                            visited[moved_r][moved_c] = 1
                            to_erase.append([moved_r, moved_c])
    return to_erase

def erase(g, erase_list):
    for r, c in erase_list:
        g[r][c] = 0
    return g

def mean_function(g):
    flag = 0
    total_sum = 0
    cnt = 0
    for g_index in range(N):
        g_row = g[g_index]

        for i in g_row:
            if i != 0:
                total_sum += i
                cnt += 1
    if total_sum != 0:
        mean = total_sum / cnt

        for g_idx in range(N):
            g[g_idx] = deque([0 if gg == 0 else gg -1 if gg > mean else gg + 1 if gg < mean else gg for gg in g[g_idx]])
    else:
        flag = 1
            
    return g, flag

def sum_function(g):
    total = 0
    for g_row in g:
        total += sum(g_row)
    return total

flag = 0         
for x, d, k in xdk:
    graph = rotate(graph, x, d, k)
    erase_cand = candidate(graph)
    if erase_cand:
        graph = erase(graph, erase_cand)
    else:
        graph, flag = mean_function(graph)
        if flag:
            break
if flag:
    total = 0
else:
    total = sum_function(graph)
print(total)