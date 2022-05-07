N, S = map(int, input().split())
nums = list(map(int, input().split()))

answer = []
cnt = 0
# N, M은 range로 처리할 수 있었지만,
# 리스트에 대한 조합은 인덱스를 받아야 한다

# sum을 global로 잡는 경우는 '최대'의 경우이며
# 현재는 모든 경우를 파악해야하니, global을 사용하면 안된다.

def dfs(idx, total_sum):
    global cnt
    if idx >= N:
        return
    
    if total_sum + nums[idx] == S:
        cnt += 1
    print(f'idx + 1, total_sum: {idx + 1, total_sum}')
    dfs(idx + 1, total_sum)
    print(f'idx + 1, total_sum + nums[idx]: {idx + 1, total_sum + nums[idx]}')
    dfs(idx + 1, total_sum + nums[idx])

dfs(0,0)
print(cnt)
    



