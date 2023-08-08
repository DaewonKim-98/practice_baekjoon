M, N = map(int, input().split())

# 2차원 배열을 만든다.
arr = []
for i in range(M):
    arr += [[0] * (N)]

# 시계방향으로 달팽이 모양이 움직이므로 방향을 설정한다.
dcoor = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# 처음 시작 칸은 0, 0
r = 0
c = 0
arr[0][0] = 1
dir = 0
# 꺾는 횟수를 cnt
cnt = 0
# 모든 칸이 채워질 때까지 반복문을 돌린다.
room = 1
while room < M * N:
    nr = r + dcoor[dir][0]
    nc = c + dcoor[dir][1]
    # 다음 조사 위치가 0보다 크거나 같고, M, N 보다 작다면 / 그리고 다음 위치가 0이면
    if 0 <= nr < M and 0 <= nc < N and arr[nr][nc] == 0:
        room += 1
        arr[nr][nc] = 1
        r, c = nr, nc

    # 더 이상 해당 방향으로 이동해 기록할 수 없을 때 방향을 바꾸고 꺾는 횟수 증가
    else:
        dir += 1
        cnt += 1
        if dir >= 4:
            dir = 0

print(cnt)