'''
1. 궁수는 3명
2. 사거리: D

3. 거리가 D 이하인 적 중 가장 가까운 적 공격, 가장 왼쪽에 있는 적
4. 같은 적이 여러 궁수에게 공격 당할 수도 있다.

5. 궁수 공격 끝나면 적 이동.
6. 한칸 이동 하는데 마지막까지 도달하면 사라진다.

'''
from copy import deepcopy
dx = [-1,-1,-1]
dy = [-1,0,1]

N, M, D = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]


def move_enemy(g):
    new_graph = [[0 for _ in range(M)] for _ in range(N)]
    for n in range(N):
        for m in range(M):
            if g[n][m]:
                if n < N-1:
                    new_graph[n+1][m] = 1
    return new_graph

def shoot(g, archers):
    cnt = 0
    
    kill_list = []
    for arch in archers:
        shoot_col = arch 

        position = []
        for n in range(N):
            for m in range(M):
                if g[n][m]:
                    distance = abs(N-n) + abs(shoot_col-m)
                    if distance <= D:
                        position.append([n,m,distance])
        if position:
            position.sort(key = lambda x: [x[2], x[1]])
            if position[0][:2] not in kill_list:
                kill_list.append(position[0][:2])
    
    for kill in kill_list:
        g[kill[0]][kill[1]] = 0
        cnt += 1
    
    return g, cnt



max_kill = 0
for i in range(M-2):
    for j in range(i+1, M-1):
        for k in range(j+1, M):
            archers = [i,j,k]
            current_kill = 0
            current_graph = deepcopy(graph)

            while True:
                flag = 1
                current_graph, killed = shoot(current_graph, archers)
                current_graph = move_enemy(current_graph)

                current_kill += killed

                for r in range(N):
                    for c in range(M):
                        if current_graph[r][c]:
                            flag = 0
                            break
                
                if flag:
                    break
            max_kill = max(max_kill, current_kill)

print(max_kill)