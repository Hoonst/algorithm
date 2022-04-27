from multiprocessing.connection import answer_challenge


R, C = map(int, input().split())

graph = [list(input()) for _ in range(R)]

answer = 0

dx = [0,0,-1,1]
dy = [-1,1,0,0]

alphas = []

def dfs(x, y, count):
    global answer

    answer = max(answer, count)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and not graph[nx][ny] in alphas:
            alphas.append(graph[nx][ny])
            dfs(nx, ny, count+1)
            print(graph[nx][ny])
            poped = alphas.pop()
            print(f'poped: {poped}')

alphas.append(graph[0][0])
dfs(0,0,1)
print(answer)
