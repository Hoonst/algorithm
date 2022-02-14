from collections import deque
N,K = map(int, input().split())

cnt = 0
deck = deque(range(1, N+1))
answer = []
while deck:
    cnt += 1
    if cnt % K == 0:
        answer.append(str(deck.popleft()))
    else:
        deck.append(deck.popleft())
print('<'+(', '.join(answer))+'>')