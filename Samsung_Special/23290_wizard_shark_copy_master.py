from copy import deepcopy
from collections import deque

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

smell = [[0] * 4 for _ in range(4)]
fish = [[[] for _ in range(4)] for _ in range(4)]
m, s = map(int, input().split())
for _ in range(m):
    x, y, d = map(int, input().split())
    fish[x-1][y-1].append(d-1)

sx, sy = map(int, input().split())
sx -= 1
sy -= 1