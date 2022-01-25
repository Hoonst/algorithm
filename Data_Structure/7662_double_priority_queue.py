'''
heap = priorityqueue

우선순위 queue는 기본적으로 heap라는 것은 알았지만, 만약 단순 힙을 구현하는 문제였다면 class 3에도 있지 않았기에 고민을 좀 했다.
내가 파악하지 못한 부분은 두 힙 값의 싱크를 맞춰주는 것으로, 이를 recorded로 나타냈다.

하나의 heap (max)에서 값이 사라진다면 다른 heap (min)에서도 역시 값이 사라지도록 설정한다.
재밌는 문제이며, 하나의 유형으로 가치가 큰 것 같다.
'''

import heapq
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    heap_max, heap_min = [], []
    func_len = int(input())
    recorded = [False] * func_len
    for j in range(func_len):
        func, value = input().split()
        value = int(value)
        
        if func == 'I':
            heapq.heappush(heap_max, (-value, j))
            heapq.heappush(heap_min, (value, j))
            recorded[j] = True
        elif func == 'D':
            # 1. 먼저 두 heap의 Sync를 맞춰준다: 즉, 두 리스트의 값을 동일하게 하는 과정
            # 2. 그 이후에도 heap에 값이 남아있다면 제거
            if value == 1:
                # 1번 과정
                while heap_max and not recorded[heap_max[0][1]]:
                    heapq.heappop(heap_max)
                # 2번 과정
                if heap_max:
                    recorded[heap_max[0][1]] = False
                    heapq.heappop(heap_max)
                
            elif value == -1:
                # 1번 과정
                while heap_min and not recorded[heap_min[0][1]]:
                    heapq.heappop(heap_min)
                # 2번 과정
                if heap_min:
                    recorded[heap_min[0][1]] = False
                    heapq.heappop(heap_min)

    while heap_max and not recorded[heap_max[0][1]]:
        heapq.heappop(heap_max)
    while heap_min and not recorded[heap_min[0][1]]:
        heapq.heappop(heap_min)
    if heap_max and heap_min:
        print(-heapq.heappop(heap_max)[0], heapq.heappop(heap_min)[0])
    else:
        print('EMPTY')