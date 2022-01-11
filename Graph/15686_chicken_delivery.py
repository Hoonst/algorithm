from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
chicken_map = [list(map(int, input().split())) for _ in range(N)]

# 여기서 두 번 돌아서 시간이 더 걸리는 것일까?
chicken, houses = [], []

for r in range(N):
    for c in range(N):
        if chicken_map[r][c] == 1:
            houses.append((r,c))
        elif chicken_map[r][c] == 2:
            chicken.append((r,c))

# chicken = [(i,j) for i in range(len(chicken_map)) for j in range(len(chicken_map[i])) if chicken_map[i][j] == 2]
# houses = [(i,j) for i in range(len(chicken_map)) for j in range(len(chicken_map[i])) if chicken_map[i][j] == 1]

chicken_remains = combinations(chicken, M)

min_total_chick_dist = float('inf')
for chicken_remain in chicken_remains:
    total_chick_dist = 0
    # 집집마다
    for hy, hx in houses:
        min_chick_dist = float('inf')
        # 치킨 집과의 거리 계산
        for cy, cx in chicken_remain:
            chick_dist = abs(cy-hy) + abs(cx-hx)
            if chick_dist < min_chick_dist:
                min_chick_dist = chick_dist
        total_chick_dist += min_chick_dist
    # total_chick_dist: 해당 치킨 집 조합에서 얻을 수 있는 도시의 치킨 거리
    if total_chick_dist < min_total_chick_dist:
        min_total_chick_dist = total_chick_dist

print(min_total_chick_dist)

# for 반복문을 계속 사용하고 있는데, 이로 인해 연산 효율성이 매우 안좋게 나타나 실행 속도가 100대로 나타나는
# 다른 답에 비해 나의 풀이는 500ms로 나타난다.

# 이 원인은 map / zip, unzip을 활용하는 다른 코드들로 인한 차이라고 생각한다. 