N = 5
board = [[0] * N for _ in range(N)]
 
#      ←   ↓   →   ↑ (4방향, 시작방향: 서쪽)
dy = ( 0,  1,  0, -1)
dx = (-1,  0,  1,  0)
 
 
def init_grid():
    y = x = int(N / 2) # 배열의 중앙 좌표
    direction = move_count = number = 0
    dist = 1
 
    while True:
        move_count += 1 # 움직인 횟수
        for _ in range(dist): # dist만큼 direction 방향으로 이동
            ny = y + dy[direction]
            nx = x + dx[direction]
 
            # 종료 조건 : 이동한 좌표가 (0, -1)인 경우(배열의 길이가 홀수면 항상 마지막 좌표는 (0, -1), 방향은 서쪽
            if (ny, nx) == (0, -1):
                return
            # 번호 증가 및 기록
            number += 1
            board[ny][nx] = number
 
            # (y, x) 갱신
            y = ny
            x = nx
 
        if move_count == 2: # 어떠한 방향으로든 2번 이동한 경우
            dist += 1 # 이동거리 1 증가
            move_count = 0 # 초기화
        direction = (direction + 1) % 4 # 방향 변경
 
init_grid()
for row in board:
    print(row)