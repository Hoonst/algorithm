'''
1. 개강총회 시작 전: 입장 여부 확인 = 개강총회 시작 이전에 대화한 적있는 학회원 닉네임 
2. 개강 총회 끝 ~ 스트리밍 대화
'''
S, E, Q = input().split()
S_time = int(''.join(S.split(':')))
E_time = int(''.join(E.split(':')))
Q_time = int(''.join(Q.split(':')))

members = []
ins = set()
outs = set()

while True:
    try:
        time, member = input().split()
        time = int(''.join(time.split(':')))
        members.append([time, member])
    except:
        break

for t, m in members:
    if t <= S_time:
        ins.add(m)
    elif E_time <= t <= Q_time:
        outs.add(m)

print(len(ins.intersection(outs)))