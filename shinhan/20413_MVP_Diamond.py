'''
과금별 혜택

1. 다섯 등급 : 현재 달과 지난 달, 즉 현재달을 포함한 최근 2개월간의 과금액으로 결정
2. 최대 과금 한도 = 다이아몬드 등급 기준액 까지만 과금 가능 (만원 단위로 과금)
3. 해당 달 끝나야 계산 책정

상민이가 게임을 시작하고 N 개월 동안 현금 과금

N 개월 간의 MVP 등급 기록 유출
과금액 역추적
'''

N = int(input())
used = list(map(int, input().split()))
MVP_rank = list(input())

rank_dict = {'B': [0,used[0]-1],
             'S': [used[0], used[1]-1],
             'G'  : [used[1], used[2]-1],
             'P': [used[2], used[3]-1],
             'D': [used[3], 10e9]}
max_limit = used[3]

before = 0
current = 0

max_paid = 0
for mvp in MVP_rank:
    if mvp == 'D':
        current = rank_dict[mvp][0]
        before = current
        max_paid += current

    else:
        # 현재는 한도에서 이전 달의 값을 뺀 것
        current = rank_dict[mvp][1] - before
        before = current
        max_paid += current

print(max_paid)