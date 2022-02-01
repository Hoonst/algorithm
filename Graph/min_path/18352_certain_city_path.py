import heapq

N, M, K, start = map(int, input().split())

graph = [[] for _ in range(N+1)]

for m in range(M):
    a,b = map(int, input().split())
    graph[a].append((1,b))
    
INF=1e9
distance = [INF]*(N+1)

def dijkstra(start):
    q = []
    distance = [INF] * (N+ 1)
    # start에서는 당연히 거리가 0이다.
    heapq.heappush(q, (0, start)) # (distance, node_idx)
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for node_cost, node_index in graph[now]:
            cost = dist + node_cost
            # 원래 시작점에서부터 해당 지점까지의 점수가 dist이고,
            # node_cost는 새로운 target에 대한 거리

            if distance[node_index] > cost:
                distance[node_index] = cost
                heapq.heappush(q, (cost, node_index))
    return distance   

route = dijkstra(start)

answer = [i for i in range(N+1) if route[i] == K]

if answer:
    for a in answer:
        print(a)
else:
    print(-1)