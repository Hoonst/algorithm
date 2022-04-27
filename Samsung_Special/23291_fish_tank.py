from collections import deque

def add_fish(fish_tanks):
    min_ = min(fish_tanks)
    fish_tanks = [fish+1 if fish == min_ else fish for fish in fish_tanks]
    return fish_tanks

def stack_tank(fish_graph, trial):

        
    




if __name__ == '__main__':
    '''
    N개의 어항 / 물고기 최다 어항 - 물고기 최소 어항 <= K

    정리 process
    1. 물고기가 가장 적은 어항에 한 마리 추가 
    최소의 물고기가 여러개 있으면, 모두에 한 마리씩 넣는.
    2. 어항 쌓기
    가장 왼쪽에 있는 어항을 그 어항의 오른쪽에 있는 어항 위에 올려 놓는다.
    3. 2개 이상 쌓여있는 어항을 공중 부양 시켜 90도 회전 > 어항 위에 올려 놓는다.
    4. 공중 부양 시계방향 90도 회전으로 인해 바닥에 있지 않으면 STOP
    5. 물고기 수 조절 들어갑니다.
    6. 모든 인접 두 어항: 물고기 수 차이 구한다.
    7. 이 차이를 5로 나눈 몫을 d라고 하자 > d가 0보다 크면 두 어항 중 물고기가 많은 곳에 물고기 d마리를 적은 곳에 있는 곳으로 보낸다. (동시 발생이니 저장해두어야 함)
    8. 가장 왼쪽 / 아래부터 순서대로 redistribute

    9. 공중 부양 = N/2개를 부양시켜 회전 시켜 위에 올려 놓는다.90도가 아니라 180도
    
    '''
    N, K = map(int, input().split())
    fishes = list(map(int, input().split()))
    graph = [[0 for _ in range(N)] for _ in range(N)]
    graph[-1] = fishes


    

