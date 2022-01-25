from collections import deque, defaultdict

N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

nodes = defaultdict(lambda: [])

for idx_y in range(N):
    for idx_x in range(N):
        if G[idx_y][idx_x]:
            nodes[idx_y].append(idx_x)

for key in range(N):
    visited = [0]*N
    
    queue = deque()
    queue.extend(nodes[key])
    
    while queue:
#         print(queue)
        visit_node = queue.popleft()
        if not visited[visit_node]:
            visited[visit_node] = 1
            queue.extendleft(nodes[visit_node])
    print(' '.join([str(i) for i in visited]))