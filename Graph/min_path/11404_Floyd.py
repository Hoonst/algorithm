'''
Dijkstra는 하나의 시작 노드에서 다른 노드까지 가는 데 까지 걸리는 최소 경로
Floyd Warshall은 모든 노드들 간의 최소 경로를 계산
두 개념의 아이디어는 비슷하나, 차이점이 있다고 한다 (아직 정확히 파악은 못함)

내 개인적인 판단으로는 다익스트라를 모든 노드에 적용하면 플로이드 와샬이 되는게 아닌가 싶은데...
'''



n = int(input())
m = int(input())

INF=1e9
d = [[INF for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    start, end, value= map(int, input().split())
    if d[start][end] > value:
        d[start][end] = value

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                continue
            else:
                d[a][b] = min(d[a][b], d[a][k] + d[k][b])

new_d = [[0 if i == INF else i for i in dist[1:]] for dist in d[1:]]
for distance_list in new_d:
    print(' '.join(list(map(str, distance_list))))