N = int(input())
num_list = list(map(int, input().split()))


num_list_sorted = sorted(list(set(num_list)))
# answer = [str(num_list_sorted.index(i)) for i in num_list]
# list를 사용하면 시간 초과
answer = {num_list_sorted[i]:i for i in range(len(num_list_sorted))}

for num in num_list:
    print(answer[num], end= ' ')