T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    room_no, floor = divmod(N, H)
    if floor == 0:
        floor = H
    else:
        room_no+=1
    if int(room_no) < 10:
        room_no = '0'+str(room_no)
    print(int(str(floor)+str(room_no)))