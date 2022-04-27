N, M = map(int, input().split())

answer = []
temp = []

def dfs():
    if len(temp) == M:
        print(' '.join(map(str, temp)))
        return
    
    for i in range(1, N+1):
        if len(temp) == 0 or temp[-1] <= i:
            temp.append(i)
            dfs()
            temp.pop()

dfs()    