'''
better expression
1) input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
2) if (a := int(input())):
    heapq.heappush(q, a)
'''

import heapq
import sys
heap = []
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    x = int(input())
    if x:
        heapq.heappush(heap, x)
    else:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(x)

