'''
- 문제 링크 
https://www.acmicpc.net/problem/2606

- 문제 설명
1번 컴퓨터가 바이러스에 감염되었을 때, 얼마나 퍼질지 나타내라.
즉, 그래프 탐색 기법 중, DFS / BFS에 관계 없이 연결된 노드들을 나타내라.

- 알고리즘
그래프 알고리즘

- 특이사항
탐색만 하면 되기 때문에 쉬운 문제였기에, 예제 입력에서는 빠르게 정답을 풀어냈지만 테스트 시에서는 지속적으로 실패했다. 처음에는 BFS를 통해서만 풀었는데 혹시 DFS로 풀어야 하나 싶어서 변경을 했는데도 실패.

따라서 다른 사람들의 풀이를 살펴본 결과
본인은 처음 그래프를 구축할 때 dic[a].append(b)와 같이 하나의 노드에 대해 단방향으로만 그래프를 구성했지만, 다른 사람들은 양방향으로 구성.

이것이 해답이라고 생각하는 근거는 1번 노드에서 출발해야 하는 문제에서 그래프가 1로 시작하는 것으로 나타나는 경우가 없다면 1번에서 시작을 할 수 없기 때문이 아닐까 추측한다. 

- 풀이
https://github.com/Hoonst/algorithm/blob/main/Graph/2606_virus.py
'''

# DFS
from collections import defaultdict
com = int(input())
dic = defaultdict(lambda:[])
pair = int(input())
for _ in range(pair):
    a,b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)
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