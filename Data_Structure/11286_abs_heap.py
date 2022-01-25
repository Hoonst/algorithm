'''
다른 답들은 plus_heap과 minus_heap을 나눠서 계산하는 방식을 취하지만,
본 답에서는 abs를 취한 뒤 음수인지 양수인지를 같이 저장하여,
만약 음수일 경우 음수를 붙여서 return

처음에는 heappush(value, minus)를 저장할 때,
[(1,True), (1,False)]를 저장하게 되어, (1,True)가 뽑히는 것이 아닌가 싶었는데,
첫 값이 같으면 두 번째 값 기준으로 min 값을 결정하기 때문에 괜찮다.
'''

import heapq
import io, sys, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

heap = []
N = int(input())
for _ in range(N):
    if (x:= int(input())):
        heapq.heappush(heap, (abs(x), False if x < 0 else True))
    else:
        if heap:
            heap_value, sign = heapq.heappop(heap)
            print(heap_value if sign else -heap_value)
        else:
            print(0)