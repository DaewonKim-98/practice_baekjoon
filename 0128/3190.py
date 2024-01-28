N = int(input())
K = int(input())
arr = [[0] * N for _ in range(N)]
arr[0][0] = 1
# 사과 넣기
for _ in range(K):
    a, b = map(int, input().split())
    arr[a - 1][b - 1] = -1
L = int(input())
# 시간과 방향을 딕셔너리로
change = {}
for _ in range(L):
    a, b = map(str, input().split())
    change[int(a)] = b

# 방향 오른쪽이 다음으로
dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

time = 0
i = 0
# 머리랑 꼬리
hr, hc = 0, 0
tr, tc = 0, 0
while True:
    time += 1
    nr, nc = hr + dir[i][0], hc + dir[i][1]
    # print(time, nr, nc, arr)
    # 만약 끝이아니거나 자신과 만나지 않으면
    if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] <= 0:
        # 사과를 만나면
        if arr[nr][nc] == -1:
            # 꼬리 안비우고 머리 전진
            arr[nr][nc] = time + 1
            hr, hc = nr, nc
            
        # 사과를 만나지 않으면
        else:
            arr[nr][nc] = time + 1
            hr, hc = nr, nc
            # 꼬리 비우고 다음 꼬리 갱신
            for d in dir:
                nnr, nnc = tr + d[0], tc + d[1]
                # 하나 늘어난게 다음 꼬리이므로
                if 0 <= nnr < N and 0 <= nnc < N and arr[nnr][nnc] == arr[tr][tc] + 1:
                    arr[tr][tc] = 0
                    tr, tc = nnr, nnc
                    break

        # 뱀의 방향 전환
        if time in change:
            if change[time] == 'L':
                i -= 1
                if i < 0:
                    i = 3
            else:
                i += 1
                if i == 4:
                    i = 0
                
    # 끝이거나 자신을 만나면
    else:
        break
    # print(time, arr)
    
print(time)