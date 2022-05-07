n = int(input())
k = int(input())

cards  = []
for i in range(n):
    cards.append(i)

# n개의 카드 중에서 k개를 선택하는 방법

for i in range(n):
    string = ''
    for j in range(k):
        string += str(cards[j])
    if string not in cards:
        cards.append(string)

print(len(cards))