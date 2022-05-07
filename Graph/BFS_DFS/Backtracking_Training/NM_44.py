N, M = map(int, input().split())

answer = []

def dfs():
    global answer
    if len(answer) == M:
        print(' '.join(answer))
        return
    
    for i in range(1, N+1):
        if not answer:
            answer.append(str(i))
            dfs()
            answer.pop()
        elif answer and int(answer[-1]) <= i:
            answer.append(str(i))
            dfs()
            answer.pop()

dfs()