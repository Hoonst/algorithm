N = int(input())

a = [list(map(int, input().split())) for _ in range(N)]
select = []

def dfs(idx, cnt):
    global ans
    if cnt == N // 2:
        start, link = 0,0
        for i in range(N):
            for j in range(N):
                if select[i] and select[j]:
                    start += select[i][j]
                elif not select[i] and not select[j]:
                    link += select[i][j]
        ans = min(ans, abs(start - link))
    
    for i in range(idx, N):
        if select[i]:
            continue
        select[i]  =1
        dfs(i+1, cnt+1)
        select[i] = 0

ans = 10e9
dfs(0,0)
print(ans)

