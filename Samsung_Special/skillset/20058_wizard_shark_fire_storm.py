from copy import deepcopy
N, Q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(2**N)]
Ls = list(map(int, input().split()))


def rotate90(g):
    g = deepcopy(g)

    gg = list(zip(*g))
    gg = [list(i[::-1]) for i in gg]

    return gg

def split_grid(g, L):
    L_square = 2**L
    N_square = 2**N
    
    new_grid = [[0 for _ in range(2**N)] for _ in range(2**N)]

    for i in range(0,N_square, L_square):
        for j in range(0,N_square, L_square):
            subset = [row[j:j+L_square] for row in g[i:i+L_square]]
            subset = rotate90(subset)

            for a in range(L_square):
                for b in range(L_square):
                     new_grid[i+a][j+b]= subset[a][b]

    return new_grid

split_grid(grid, 1)

    

