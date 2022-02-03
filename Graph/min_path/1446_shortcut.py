'''
shortcut을 미리 구할 때, 아래 조건에 걸리면 지름길로 간주하지 않는다.
1) 지름길로 가는게 더 오래 걸리는 경우
2) 도착지점이 D보다 큰 경우

알고리즘
1. N 지점의 거리는 (N-1)의 거리 + 1이다.
2. 현재 도착지점이 지름길의 도착지점 중 포함되어 있다면,
    > 지름길 도착지점과 쌍을 이루고 있는 지름길 출발 지점에서 지름길 길이를 더한 것
    > 이전 지점에서 + 1을 한 것 (미리 구해져 있는 값)을 비교
    최소값을 구한다.
'''

N, D = map(int, input().split())

shortcut = []
for _ in range(N):
    start, end, length = map(int, input().split())
    if end-start < length or end > D:
        continue
    else:
        shortcut.append((start,end,length))
        
graph = [0] * (D+1)

for index in range(1,D+1):
    graph[index] = graph[index-1] + 1
    for short in shortcut:
        if short[1] == index:
            graph[index] = min(graph[short[0]] + short[2], graph[index])
            
print(graph[D])

