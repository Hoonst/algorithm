# 21609 상어 중학교

grid = [[2,2,-1,3,1],
        [-2,-2,2,0,-1],
        [-2,-2,-2,1,2],
        [-1,-2,1,3,2],
        [-2,-2,2,2,1]]

# 입력에 대한 변화 test


def gravity(g):
    N = len(g)

    for column in range(N):
        for floor in range(N-2,-1,-1):
            # 현재 층이 자연수이고, 다음 층이 빈 공간일 때
            if g[floor][column] > -1 and g[floor+1][column] < -1:

                # 다음 층부터 수색
                for i in range(floor+1, N):
                    if g[i][column] > -2:
                        if i == N-1:
                            g[i][column] = g[floor][column]
                        else:
                            g[i-1][column] = g[floor][column]
                        g[floor][column] = -2

                        break

    return g

for row in grid:
    print(row)

print('='*30)

for row in gravity(grid):
    print(row)
