# target = [i for i in range(10)]
# visited = [0 for _ in range(10)]
# length = 4
# answer = []

# def dfs(cnt, target):
#     if cnt == r:
#         answer.append(target[:])
#         return

#     for i, val in enumerate(l):
#         # 중복 순열을 만들고 싶다면 visited에 대한 기록을 삭제
#         # if visited[i] == 1:
#         #     continue

#         target.append(val)
#         visited[i] = 1

#         dfs(cnt + 1, target)

#         target.pop()
#         visited[i] = 0

# dfs(0, [])

# print(answer)
# for p in answer:
#     print(p)

target = [i for i in range(5)]
visited = [0 for _ in range(5)]
length = 3
answer = []

def permutation_dfs(temp):
    if len(temp) == length:
        answer.append(temp[:])
        return
    
    for i,val in enumerate(target):
        if visited[i] == 1:
            continue

        temp.append(val)
        visited[i] = 1

        permutation_dfs(temp)

        temp.pop()
        visited[i] = 0

permutation_dfs([])

for p in answer:
    print(p)