# sys를 사용하면 메모리가 약간 증가하지만 실행시간 절반
# DP로 분류되어 있지는 않고 재귀를 사용

import sys
from typing import List

input = sys.stdin.readline

N = int(input())
whole_paper = [list(map(int, input().split())) for _ in range(N)]
dic = {-1:0,0:0,1:0}
def cut_paper(paper: List) -> None:
    to_array = [j for i in paper for j in i]    
    
    if all([i==to_array[0] for i in to_array]):
        dic[to_array[0]]+=1
    
    elif len(to_array) == 9:
        for i in to_array:
            dic[i]+=1
        
    else:
        length_p = len(paper)
        length_cut = length_p // 3

        one   = [i[:length_cut] for i in paper[:length_cut]]
        two   = [i[length_cut:length_cut*2] for i in paper[:length_cut]]
        three = [i[length_cut*2:length_cut*3] for i in paper[:length_cut]]
        four  = [i[:length_cut] for i in paper[length_cut:length_cut*2]]
        five  = [i[length_cut:length_cut*2] for i in paper[length_cut:length_cut*2]]
        six   = [i[length_cut*2:length_cut*3] for i in paper[length_cut:length_cut*2]]
        seven = [i[:length_cut] for i in paper[length_cut*2:length_cut*3]]
        eight = [i[length_cut:length_cut*2] for i in paper[length_cut*2:length_cut*3]]
        nine  = [i[length_cut*2:length_cut*3] for i in paper[length_cut*2:length_cut*3]]
        cut_paper(one)
        cut_paper(two)
        cut_paper(three)
        cut_paper(four)
        cut_paper(five)
        cut_paper(six)
        cut_paper(seven)
        cut_paper(eight)
        cut_paper(nine)  

cut_paper(whole_paper)
print(dic[-1])
print(dic[0])
print(dic[1])