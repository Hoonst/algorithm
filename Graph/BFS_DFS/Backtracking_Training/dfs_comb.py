l = [1,2,3,4]
n = len(l)
r=3
answer = []

def dfs(idx, list):
    if len(list) == r:
        answer.append(list[:])
        return
    
    for i in range(idx, n):
        print(f'i+1: {i+1}')
        print(f'idx: {idx}')
        print(f'n: {n}')
        print(list+[l[i]])
        dfs(i+1, list+[l[i]])

dfs(0, [])

'''
빈 공간부터 하나씩 더해가면서,
조건을 만족하면 해당 Path는 아웃
'''