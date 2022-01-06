# p.96 숫자 카드 게임
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

minmax = max(list(map(min, graph)))
print(minmax)