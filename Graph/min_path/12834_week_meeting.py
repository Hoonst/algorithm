import heapq
N, V, E = map(int, input().split())

A, B = map(int, input().split())
team_home = list(map(int, input().split()))

graph = [[] for _ in range(V+1)]

for _ in range(E):
    a,b,l = map(int, input().split())
    graph[a].append((l,b))
    graph[b].append((l,a))

def dijkstra(start): 
    q = []
    distance = [INF] * (V+ 1)
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

INF=1e9  
answer = 0
for start in team_home:
    d = dijkstra(start)
    a = d[A] if d[A] != INF else -1
    b = d[B] if d[B] != INF else -1
    
    answer += (a+b)
print(answer) 