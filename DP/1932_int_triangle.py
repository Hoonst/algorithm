'''
- 문제 링크 
https://www.acmicpc.net/problem/1932

- 문제 설명
정수로 이루어진 삼각형에 대하여, 첫 층에서 맨 아래 층까지 더해나갈 때, 마지막 층의 가장 큰 숫자를 구하시오

- 알고리즘
DP

- 특이사항
정수 삼각형의 외각 (0, len(list)-1) 부분은 이전 층과 현재 층의 값을 바로 더한다. 중간 요소들은 이전 층의 좌, 우를 더한 값 중에서 Max를 비교하여 저장한다.

대각선으로 빠지는 외각도로는 상관 없다.  
중간 내부도로를 타는 녀석들은 Max를 사용한다.

- 시간 복잡도
O(N^2)

'''

n = int(input())
tree = [list(map(int, input().split())) for _ in range(n)]

def answer(input_tree):
    for tree_index in range(1, len(input_tree)):
        for leaf_index in range(len(input_tree[tree_index])):

            past_layer = input_tree[tree_index-1]
            current_layer = input_tree[tree_index]

            if leaf_index == 0:
                current_layer[leaf_index] += past_layer[leaf_index]
            elif leaf_index == len(current_layer)-1:
                current_layer[leaf_index] += past_layer[len(past_layer)-1]
            else:
                current_layer[leaf_index] = max(current_layer[leaf_index] + past_layer[leaf_index-1], current_layer[leaf_index] + past_layer[leaf_index])
    return input_tree[-1]   

print(max(answer(tree)))