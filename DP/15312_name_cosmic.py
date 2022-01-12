# 15312. 이름 궁합
# link: https://www.acmicpc.net/problem/15312
import string

A = input()
B = input()

writing = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
alpha_dic = {key:write for key, write in zip(string.ascii_uppercase, writing)}
A_list, B_list = [alpha_dic[i] for i in A], [alpha_dic[j] for j in B]

name_combined = []
for i,j in zip(A, B):
    name_combined.append(alpha_dic[i])
    name_combined.append(alpha_dic[j])

while len(name_combined) > 2:
    name_combined = [int(str(name_combined[idx] + name_combined[idx-1])[-1]) for idx in range(1, len(name_combined))]
answer = ''.join(list(map(str, name_combined)))
print(answer)
