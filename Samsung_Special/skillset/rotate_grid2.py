from copy import deepcopy
original_grid = [[i for i in range(5*(j-1), 5*j)] for j in range(1,6)]

print('Rotate Grid Clockwise')
grid = deepcopy(original_grid)
for g in grid:
    print(g)
grid = list(zip(*grid))[::-1]
grid = [list(s) for s in grid]
for g in grid:
    print(g)

print('='*30)

print('Rotate Grid Counter Clockwise')
grid = deepcopy(original_grid)
for g in grid:
    print(g)
grid = list(zip(*grid))
grid = [list(s)[::-1] for s in grid]
for g in grid:
    print(g)