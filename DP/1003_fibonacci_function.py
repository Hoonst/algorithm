
# T = int(input())

# def fibonacci(n: int) -> int:
#     if n == 0:
#         global zero
#         zero += 1
#         return 0
#     elif n == 1:
#         global one
#         one +=1
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
    
# for _ in range(T):
#     zero = 0
#     one = 0
#     fibonacci(int(input()))
#     print(zero, one)

T = int(input())

def fibonacci(n: int) -> int:
    temp = [0 for _ in range(n+1)]
    if n > 0:
        temp[1] = 1
        for i in range(2, n+1):
            temp[i] = temp[i-1] + temp[i-2]
    else:
        return [1,0]
    return temp

for _ in range(T):
    num = int(input())
    a,b = fibonacci(num)[-2:]
    print(a,b)