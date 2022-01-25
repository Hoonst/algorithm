import heapq
import io, sys, os
heap = []
#input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    if (x:= int(input())):
        heapq.heappush(heap, -x)
    else:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(0)