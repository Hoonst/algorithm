target = list(range(10))
length = 4
answer = []

def dfs(idx, t):
    if len(t) == length:
        answer.append(t)
        return
    
    for i in range(idx, len(target)):
        dfs(i+1, t + [target[i]])

dfs(0, [])
print(answer)

target = list(range(10))
visited = [0 for _ in range(10)]
answer = []
length = 4

def permutation(cnt, temp):
    if len(temp) == length:
        answer.append(temp)
        return
    
    for i, val in enumerate(target):
        if visited[i] == 1:
            continue

        visited[i] = 1
        temp.append(val)

        dfs(cnt+1, temp)

        visited[i] = 0
        temp.pop()