N, M, x, y, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
order = list(map(int, input().split()))

# 동 1, 서 2, 북 3, 남 4
# 주사위
dice = [0, [0, 0, 0], 0, 0]

for dir in order:
    if dir == 4:
        # 지도를 벗어나지 않으면
        if x + 1 < N:
            # 좌표 변경
            x = x + 1
            # 주사위 굴리기
            # 굴렸을 때 위쪽을 up으로
            up = dice[0]
            dice[0] = dice[3]
            dice[3] = dice[2]
            dice[2] = dice[1][1]
            dice[1][1] = up
            print(up)
            # 주사위를 놓은 곳의 좌표가 0이면
            if arr[x][y] == 0:
                arr[x][y] = dice[3]
            # 0이 아니면
            else:
                dice[3] = arr[x][y]
                arr[x][y] = 0
                
    elif dir == 3:
        # 지도를 벗어나지 않으면
        if x - 1 >= 0:
            # 좌표 변경
            x = x - 1
            # 주사위 굴리기
            # 굴렸을 때 위쪽을 up으로
            up = dice[2]
            dice[2] = dice[3]
            dice[3] = dice[0]
            dice[0] = dice[1][1]
            dice[1][1] = up
            print(up)
            # 주사위를 놓은 곳의 좌표가 0이면
            if arr[x][y] == 0:
                arr[x][y] = dice[3]
            # 0이 아니면
            else:
                dice[3] = arr[x][y]
                arr[x][y] = 0
                
    elif dir == 2:
        # 지도를 벗어나지 않으면
        if y - 1 >= 0:
            # 좌표 변경
            y = y - 1
            # 주사위 굴리기
            # 굴렸을 때 위쪽을 up으로
            up = dice[1][2]
            dice[1][2] = dice[3]
            dice[3] = dice[1][0]
            dice[1][0] = dice[1][1]
            dice[1][1] = up
            print(up)
            # 주사위를 놓은 곳의 좌표가 0이면
            if arr[x][y] == 0:
                arr[x][y] = dice[3]
            # 0이 아니면
            else:
                dice[3] = arr[x][y]
                arr[x][y] = 0
                
    elif dir == 1:
        # 지도를 벗어나지 않으면
        if y + 1 < M:
            # 좌표 변경
            y = y + 1
            # 주사위 굴리기
            # 굴렸을 때 위쪽을 up으로
            up = dice[1][0]
            dice[1][0] = dice[3]
            dice[3] = dice[1][2]
            dice[1][2] = dice[1][1]
            dice[1][1] = up
            print(up)
            # 주사위를 놓은 곳의 좌표가 0이면
            if arr[x][y] == 0:
                arr[x][y] = dice[3]
            # 0이 아니면
            else:
                dice[3] = arr[x][y]
                arr[x][y] = 0
        