'''
이 문제는 뭔가 이해가 될 것 같지만,  
알고리즘 시험 문제에서는 나오지 않을 것 같아 패스
'''

# 단순 반복으로 하면 무조건 시간초과
T = int(input())
for _ in range(T):
    M,N,x,y = map(int, input().split())
    a,b = (1,1)
    total = 1
    while total <= M*N:
        if a < M:
            a += 1
        else:
            a = 1
        if b < N:
            b += 1
        else:
            b = 1
            
        total += 1
            
        if (a == x) & (b == y):
            break
    if (a != x) or (b != y):
        print(-1)
    else:
        print(total)

def num(m, n, x, y):
    while x <= m * n:
        if (x - y) % n == 0:
            return x
        x += m
    return -1

t = int(input())
for i in range(t):
    m, n, x, y = map(int, input().split())
    print(num(m, n, x, y))