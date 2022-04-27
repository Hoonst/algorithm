N = int(input())

num_list = [list(map(int, input().split())) for _ in range(N)]

for nums in range(len(num_list)):
    print(f'#{nums+1} {sum([i for i in num_list[nums] if i % 2 != 0])}')
