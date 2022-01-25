'''
특이사항:
reverse가 들어가는 문제라고 해서 마냥 좋다고 바로 list.reverse()를 적용하는 것은 옳지 않다.
O(N) 만큼의 시간 복잡도가 추가되기 때문에 우회하는 방식을 떠올릴 수 있다면 적용하는 것이 좋다.

해당 문제가 그런 경우인데 
1) RR이 두번 등장하면 원상태이므로 p에서 제거하는 방법
2) R의 여부에 따라 앞과 뒤의 값을 하나씩 뺴주는 방법
을 생각해볼 수 있다.
'''
from collections import deque

def AC(ps, arrays):
    left_flag = True
    for p in ps:
        if p == 'R': left_flag = not left_flag
        elif p =='D':
            if not arrays or arrays[0] == '':
                return 'error'
            if left_flag:
                arrays.popleft()
            else:
                arrays.pop()        
    if not left_flag:
        arrays.reverse()
    if arrays:
        arrays = list(map(str, arrays))
    arrays ='['+','.join(arrays)+']'
    
    return arrays

T = int(input())
for _ in range(T):
    p = input()
    # 'RR'이면 그대로이니, 처리를 안 해주고 빼준다는 생각을 왜 못했는지...
    # p = input().replace('RR', '').split('R')    
    n = int(input())
    array = deque(input()[1:-1].split(','))
    print(AC(p, array))

'''
# 1위 답안
for _ in range(int(input())):
    f=list(map(len,input().replace('RR','').split('R')))
    n=int(input())
    a=input()[1:-1].split(',')
    s,e=sum(f[0::2]),n-sum(f[1::2])
    a=a[s:e] if len(f)%2==1 else a[s:e][::-1]
    print(f"[{','.join(a)}]" if s<=e else "error")
'''
