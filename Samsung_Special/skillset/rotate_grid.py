from pprint import pprint

grid = [[i for i in range(5*(j-1), 5*j)] for j in range(1,6)]

def rotate_90(g):
    N = len(g)

    ret = [[0 for _ in range(N)] for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = g[r][c]
    return ret

def rotate_90_(g):
    N = len(g)

    ret = [[0 for _ in range(N)] for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[N-1-c][r] = g[r][c]
    return ret

print('Rotation 90')
for i in rotate_90(grid):
    print(i, '\n')

print('Rotation -90')
for j in rotate_90_(grid):
    print(j, '\n')

# print(f'rotate_90: {rotate_90(grid)}')
# pprint(f'rotate_90_: {rotate_90_(grid)}')