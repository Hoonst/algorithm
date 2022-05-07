target = [i for i in range(10)]
length = 4
answer = []

# def dfs(idx, list):
#     if len(list) == length:
#         answer.append(list)
#         return

#     for i in range(idx, len(target)):
#         print(f'i+1, list+[l[i]]: {i+1, list+[target[i]]}')
#         dfs(i+1, list+[target[i]])

# dfs(0, [])
# print(answer)

def combination_dfs(idx, temp_list):
    if len(temp_list) == length:
        answer.append(temp_list)
        return

    # 중복 조합은 i+1을 i로 격하
    for i in range(idx, len(target)):
        print(f'Start with idx : {idx}')
        print(f'From list {temp_list} > {temp_list + [target[i]]}')
        combination_dfs(i, temp_list+[target[i]])

combination_dfs(0, [])
print(answer)


