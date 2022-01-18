# 에라토스테네스의 체를 통해
# 소수들의 배수를 삭제해 나가는 방식을 사용했는데
# 이상하게 90%대에서 오답이 나타난다...
import math
M, N = map(int, input().split())

def primary(n):
    array = [True] * (n+1)
    for i in range(2, n+1):
        if array[i] == True:
            j = 2
            while i * j <= n:
                array[i*j] = False
                j += 1
    return array
            
answer = primary(N)
for i in range(M, len(answer)):
    if answer[i]:
        print(i)

# 제출 답안
def isPrime(num):
    if num==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return False
        return True

M, N = map(int, input().split())

for i in range(M, N+1):
    if isPrime(i):
        print(i)