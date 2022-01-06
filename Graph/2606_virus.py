
# DFS
from collections import defaultdict
com = int(input())
dic = defaultdict(lambda:[])
pair = int(input())
for _ in range(pair):
    a,b = map(int, input().split())
    dic[a].append(b)

visited = [0 for i in range(com)]

def dfs(x:int) -> None:
    visited[x-1] = 1
    for i in dic[x]:
        if visited[i-1] == 0:
            dfs(i)        
            
dfs(1)
print(sum(visited)-1)

# BFS
from collections import defaultdict, deque
com = int(input())
dic = defaultdict(lambda:set())
pair = int(input())
for _ in range(pair):
    a,b = map(int, input().split())
    dic[a].add(b)
    dic[b].add(a)

visited = [0 for i in range(com)]
visited[0] = 1

# bfs를 통해 visited를 계산하고 총합-1
def bfs(x:int) -> None:
    queue = deque()
    queue.extend(dic[x])
    while queue:
        target = queue.popleft()
        if visited[target-1] == 0:
            visited[target-1] = 1
            for d in dic[target]:
                if visited[d-1] == 0:
                    queue.append(d)
        
bfs(1)
print(sum(visited)-1)