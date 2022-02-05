INF=1e9

N, M = map(int, input().split())
d = [[INF for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    start, end = map(int, input().split())
    d[start][end] = 1
    d[end][start] = 1

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            if a == b:
                d[a][b] = 0
            else:
                d[a][b] = min(d[a][b], d[a][k] + d[k][b])
                
d = [sum(i[1:]) for i in d[1:]]
min_value = min(d)

for i in range(len(d)):
    if d[i] == min_value:
        print(i)
        break