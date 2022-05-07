# 함수의 input으로 행렬을 넣었을 때,
# input을 변화시키면 행렬도 함께 변하는가?
import copy

grid = [[2,2,-1,3,1],
        [-2,-2,2,0,-1],
        [-2,-2,-2,1,2],
        [-1,-2,1,3,2],
        [-2,-2,2,2,1]]

def grid_change(g):
    N, M = len(g), len(g[0])
    for r in range(N):
        for c in range(M):
            g[r][c] += 1
    
    return g

def grid_change_copy(g):
    g = g.copy()

    N, M = len(g), len(g[0])
    for r in range(N):
        for c in range(M):
            g[r][c] += 1
    
    return g

def grid_change_deepcopy(g):
    g = copy.deepcopy(g)

    N, M = len(g), len(g[0])
    for r in range(N):
        for c in range(M):
            g[r][c] += 1
    
    return g


print('original grid')
for i in grid:
    print(i)
print('='* 20)

grid = [[2,2,-1,3,1],
        [-2,-2,2,0,-1],
        [-2,-2,-2,1,2],
        [-1,-2,1,3,2],
        [-2,-2,2,2,1]]
changed_grid = grid_change(grid)

print('no copy')
for i in changed_grid:
    print(i)
print('grid')
for j in grid:
    print(j)
print('='* 20)
print('copy')
grid = [[2,2,-1,3,1],
        [-2,-2,2,0,-1],
        [-2,-2,-2,1,2],
        [-1,-2,1,3,2],
        [-2,-2,2,2,1]]
copied_grid = grid_change_copy(grid)
for c in copied_grid:
    print(c)
print('='* 20)
print('grid')
for j in grid:
    print(j)
print('deepcopy')
grid = [[2,2,-1,3,1],
        [-2,-2,2,0,-1],
        [-2,-2,-2,1,2],
        [-1,-2,1,3,2],
        [-2,-2,2,2,1]]
deepcopied_grid = grid_change_deepcopy(grid)
for d in deepcopied_grid:
    print(d)

print('='* 20)
for j in grid:
    print(j)
print('')
