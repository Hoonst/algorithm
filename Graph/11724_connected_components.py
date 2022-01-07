from collections import defaultdict, deque
import sys
input = sys.stdin.readline

node, edge = map(int, input().split())
dic = defaultdict(lambda:set())

for _ in range(edge):
    a,b = map(int, input().split())
    dic[a].add(b)
    dic[b].add(a)

visited = [0 for i in range(node)]
visited_node = []

# # bfs를 통해 visited를 계산하고 총합-1
# def bfs(x:int) -> None:
#     queue = deque()
#     queue.extend(list(dic[x]))
#     while queue:
#         target = queue.popleft()
#         if visited[target-1] == 0:
#             visited[target-1] = 1
#             visited_node.append(target)
#             for d in dic[target]:
#                 if visited[d-1] == 0:
#                     queue.append(d)

def dfs(x:int) -> None:
    visited[x-1] = 1
    visited_node.append(x)
    for i in dic[x]:
        if visited[i-1] == 0:
            dfs(i)        
            
answer = 0
key = 1
while len(visited_node) < node:
    if key not in visited_node:
        dfs(key)
        answer += 1
    key+=1
    
print(answer)