'''
참고 자료: https://daimhada.tistory.com/181
'''

N = int(input())
stairs = [int(input()) for _ in range(N)]
dp = []

if N >= 1:
    dp.append(stairs[0])
if N >= 2:
    dp.append(max(stairs[0] + stairs[1], stairs[1]))
if N >= 3:
    dp.append(max(stairs[0] + stairs[2], stairs[1] + stairs[2]))

for i in range(3, N):
    dp.append(max(dp[i-2] + stairs[i], dp[i-3] + stairs[i] + stairs[i-1]))

print(dp.pop())