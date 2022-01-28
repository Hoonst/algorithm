'''
11053. 가장 긴 증가하는 부분 수열
해당 문제는 DP의 유형을 가지며,
[10,20,10,30,20,50]의 예시로 보자

기본적인 골자는 리스트의 인덱스를 순회하며, 해당 인덱스 이전의 값들 중 현재 값보다 작다면
그 값이 지금까지 구성한 순열 길이 + 1 로 계산하는 것이다.
4번째 인덱스 30에 도착했다면, [10,20,10]이 대상인데
10은 1, 20은 10에서부터 왔으니 2, 3번째 10은 증가하는 수열이 없으므로 1일 것이다. 
따라서 20의 수열 2에다가 +1를 적용하면 30까지의 수열은 3이 되며,
3번째 10의 값이 대체되지 않도록 max function을 사용해서 조율한다.
'''

N = int(input())
A = list(map(int, input().split()))
dp = [0] * N

for A_idx in range(1, N):
    for a in range(A_idx):
        if A[a] < A[A_idx]:
            dp[A_idx] = max(dp[A_idx], dp[a]+1)


'''
# Wrong Answer!

N = int(input())
A = list(map(int, input().split()))

start_idx, max_permute = 0, 0

while start_idx < N:
    max_a , permute = 0, 0
    for datum in A[start_idx:]:
        if datum > max_a:
            max_a = datum
            permute += 1
    if permute > max_permute:
        max_permute = permute
    start_idx += 1
print(max_permute)
'''