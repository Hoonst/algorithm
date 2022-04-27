'''
16235. 나무 재테크
N x N 땅에 재테크를 시작
1. 양분 5만큼이 들어있다.
2. M개의 나무를 심는데 한 칸에 여러 나무가 존재할 수 있다.
3. 사계절을 보낸다.
    1. 봄: 자신의 나이만큼 양분 섭취 / 나이 1 증가 / 나이가 어련 녀석부터 양분을 먹는다 / 자기 나이 만큼 양분을 못먹으면 사망
    2. 여름: 봄에 죽은 나무가 양분으로 변한다 = 죽은 나무 나이 // 2가 양분으로 추가
    3. 가을: 나무 번식 = 나이가 5의 배수여야 번식이 가능 인접한 8개 칸에 나이가 1인 나무 생성
    4. 겨울: 기계가 땅에 양분 추가 / 각 칸에 추가되는 양분의 양이 다르다.

4. K년이 지난 후, 살아남은 나무의 수를 출력
'''
# N: N*N의 격자 / M: 나무 개수 / K: 몇 년 동안
from collections import deque

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

# tree_info = [list(map(int, input().split())) for _ in range(M)]
# tree_info = [[x-1,y-1,z] for x,y,z in tree_info]
tree = [[deque() for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y, z = map(int, input().split())
    tree[x-1][y-1].append(z)

land = [[5 for _ in range(N)] for _ in range(N)]

# graph: A / infos: tree_info
def spring(graph, tree_infos):
    dead_tree = {}
    for row_idx in range(N):
        for col_idx in range(N):
            if tree_infos[row_idx][col_idx]:
                plants = tree_infos[row_idx][col_idx]
                for age_index in range(len(plants)):
                    age = tree_infos[row_idx][col_idx][age_index]
                    if graph[row_idx][col_idx] >= age:
                        graph[row_idx][col_idx] -= age
                        tree_infos[row_idx][col_idx][age_index] += 1
                    else:
                        for k in range(age_index, len(plants)):
                            if (row_idx, col_idx) in dead_tree:
                                dead_tree[(row_idx, col_idx)].append(tree_infos[row_idx][col_idx].pop())
                            else:
                                dead_tree[(row_idx, col_idx)] = [tree_infos[row_idx][col_idx].pop()]
                        break
    
    return tree_infos, dead_tree, graph

def summer(graph, dead_trees):
    for tree_row, tree_col in dead_trees:
        for corpse in dead_trees[(tree_row, tree_col)]:
            graph[tree_row][tree_col] += (corpse // 2)
    return graph

def autumn(tree_infos):
    dx = [1,1,1,0,-1,-1,-1,0]
    dy = [1,0,-1,-1,-1,0,1,1]

    for row_idx in range(N):
        for col_idx in range(N):
            for z in tree_infos[row_idx][col_idx]:
                if z % 5 == 0:
                    for i in range(8):
                        if 0 <= row_idx+dx[i] < N and 0 <= col_idx+dy[i] < N:
                            tree_infos[row_idx+dx[i]][col_idx+dy[i]].appendleft(1)
    
    return tree_infos

def winter(graph, bucket):
    N = len(graph)
    for i in range(N):
        for j in range(N):
            graph[i][j] += bucket[i][j] 
    return graph

for k in range(K):
    tree, deads, land = spring(land, tree)

    land = summer(land, deads)
    tree = autumn(tree)
    land = winter(land, A)

result = 0
for i in range(N):
    for j in range(N):
        result += len(tree[i][j])
print(result)