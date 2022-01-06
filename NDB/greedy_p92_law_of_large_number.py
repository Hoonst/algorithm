N, M, K = map(int, input().split())

nums = list(map(int, input().split()))

sorted_nums = sorted(nums)[::-1]
first, second = sorted_nums[:2]

total = 0
start = time.time() 

not_change = K
for _ in range(M):
    if not_change:
        total += first
        not_change-=1
    else:
        total += second
        not_change=K
print(total)
end = time.time() 
print(f"{end - start:.5f} sec")

# 해당 방식은 시간 초과 발생 가능성이 있음
# 수학적 이론을 정립해서 풀어보자

# 8 // 3
# (6 6 6 5) (6 6 6 5)
# (first * 3 + second)가 4개로 구성되어 그것을 M으로 나눈 몫만큼 더해지고
# remainder만큼 first를 더해주면 된다. 

start = time.time() 
quotient, remainder = divmod(M, K+1)
if M >= K + 1: 
    print(quotient*(first*3+second)+first*remainder)
else:
    print(quotient*first)
end = time.time() 

print(f"{end - start:.5f} sec")

# 46
# 0.00063 sec
# 46
# 0.00015 sec