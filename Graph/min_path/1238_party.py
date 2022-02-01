import heapq

N, M, X = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, time = map(int, input().split())
    graph[start].append((end, time))

INF=1e9
distance = [INF]*(N+1)

def dijkstra(start):
    q = []
    distance = [INF] * (N+ 1)
    
    heapq.heappush(q, (0, start)) # (distance, node_idx)
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        for node_index, node_cost in graph[now]:
            cost = dist + node_cost
            # 원래 시작점에서부터 해당 지점까지의 점수가 dist이고,
            # node_cost는 새로운 target에 대한 거리
            if distance[node_index] > cost:
                distance[node_index] = cost
                heapq.heappush(q, (cost, node_index))
    return distance 

result = 0 
to_X = dijkstra(X)
for i in range(1,N+1):
    visited = [False]*(N+1)
    distance = [INF]*(N+1)
    from_X = dijkstra(i)
    result = max(result, from_X[X] + to_X[i])
print(result) 