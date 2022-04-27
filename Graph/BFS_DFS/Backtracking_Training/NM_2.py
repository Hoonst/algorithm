N, M = map(int, input().split())

temp = []
def dfs():
    if len(temp) == M:
        print(' '.join(list(map(str, temp))))
        return
    
    else:
        for i in range(N):
            if i not in temp:
                temp.append(i)
                dfs()
                temp.pop()