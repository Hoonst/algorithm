# N * N의 Grid / M개의 Limit
N, M = map(int, input().split())

chicken_map = [list(map(int, input().split())) for _ in range(N)]

chickens = []
homes = []
for r in range(N):
    for c in range(N):
        t = chicken_map[r][c]
        if t == 2:
            chickens.append([r,c])
        elif t == 1:
            homes.append([r,c])

min_score = 1e9

def bfs(chicks):
    total_score = 0
    for home in homes:
        home_x, home_y = home
        min = 1e9
        for chick in chicks:
            chick_x, chick_y = chick
            distance = abs(home_x - chick_x) + abs(home_y - chick_y)
            if distance < min:
                min = distance
        total_score += min
    return total_score

def dfs(idx, target):
    global min_score
    if len(target) == M:
        score = bfs(target)
        min_score = min(score, min_score)
        return

    for i in range(idx, len(chickens)):
        dfs(i+1, target + [chickens[i]])

dfs(0, [])

print(min_score)