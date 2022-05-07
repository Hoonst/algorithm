'''
단어를 읽는 순서 / 실제 발음을 알 수 없도록 규칙이 제각각

W를 이루고 있는 g개의 그림 문자
연구 대상인 문자열 S

단어 W가 마야 문자열에 포함되어 있을 경우
'''
from itertools import permutations


g, len_S = map(int, input().split())
W = list(input())
S = list(input())

permutation = []
# def dfs(word):
#     global permutation
#     if 

print(list(permutations(W, 1)))

for i in range(1, g+1):
    for j in permutations(W, i):
        string = ''.join(j)
        permutation.append(string)
print(permutation)

for permute in permutation:
    if permute in S:
        print(permute)