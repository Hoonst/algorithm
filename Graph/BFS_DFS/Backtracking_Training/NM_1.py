N, M = map(int, input().split())

answer = []
temp = []

def dfs():
    if len(temp) == M:
        # if sorted(temp) not in answer:
        #     answer.append(sorted(temp))
            print(' '.join(map(str, temp)))
        return
    
    for i in range(1, N+1):
        # print(f'i : {i}')
        # if i not in temp:
        temp.append(i)
        # print(temp)
        dfs()
        temp.pop()

dfs()    