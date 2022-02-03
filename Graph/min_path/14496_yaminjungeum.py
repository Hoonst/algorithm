'''
가중치가 1인 경우에는 횟수에 의하여 최소 경로가 판가름나게 되어 있지만,  
가중치가 제각각인 경우에는 지금 당장 찾은 최소 경로보다 다른 경로가 더 적게 소요될 수 있다.  

최소 경로를 구하기 위해서 가중치가 1인 경우 또는 일부 경우에서는 다익스트라 Function을 활용하는 것보다 개념만을 적용해서 풀이하는 것이 더 적은 비용을 소요할 수 있다.
'''

a,b = map(int, input().split())
N,M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append((1,end))
    graph[end].append((1,start))
    
INF=1e9
def dijkstra(start):
    import heapq
    
    q = []
    distance = [INF] * (N+1)
    heapq.heappush(q, (0, start)) # (distance, node_idx)
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for node_cost, node_index in graph[now]:
            cost = dist + node_cost
            if distance[node_index] > cost:
                distance[node_index] = cost
                heapq.heappush(q, (cost, node_index))
    return distance 

dist = dijkstra(a)
if dist[b] == INF:
    print(-1)
else:
    print(dist[b])

'''
def findRoute(a, b):
    queue = []
    queue.append((a, 0))

    visited = [False for _ in range(n + 2)]

    while(len(queue) > 0) :
        top = queue.pop(0)

        if top[0] == b:
            return top[1]
            

        for i in change[top[0]]:
            if visited[i] == False:
                visited[i] = True
                queue.append((i, top[1] + 1))

    return -1
'''