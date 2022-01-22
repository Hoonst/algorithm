# 일반적인 재귀는 TIMEout 발생
# T = int(input())

# def dp(n):
#     if n < 4:
#         return 1
#     elif n in [4,5]:
#         return 2
#     else:
#         return dp(n-1) + dp(n-5)

# for _ in range(T):
#     print(dp(int(input())))

# Memoization도 가능
# T = int(input())

# def dp_memo(n, table):
#     if table[n]:
#         return table[n]
#     table[n] = dp_memo(n-1, table) + dp_memo(n-5, table)
    
#     return table[n]

# for _ in range(T):
#     table = [0,1,1,1,2,2]+([0]*100)
#     print(dp_memo(int(input()), table))

T = int(input())
def dp_table(n, table):
    if n > 5:
        for i in range(6, n+1):
            table[i] = table[i-1] + table[i-5]
    return table[n]

for _ in range(T):
    table = [0,1,1,1,2,2]+([0]*100)
    print(dp_table(int(input()), table))