dir = [[], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
# 대각선 방향
dir_x = [[1, 1], [1, -1], [-1, 1], [-1, -1]]

def move_cloud(d, s):
    clouds = []
    # 처음 시행에는 생성되는 구름은 정해져 있으므로
    if cnt == 1:
        # 구름을 방향과 거리에 맞게 옮기기
        for cloud in [[N - 1, 0], [N - 2, 0], [N - 1, 1], [N - 2, 1]]:
            clouds.append([(cloud[0] + dir[d][0] * s) % N, (cloud[1] + dir[d][1] * s) % N])
    # 나머지 생성되는 구름은 저장된 물이 2 이상인 칸들이므로
    else:
        for r in range(N):
            for c in range(N):
                # 물이 2 이상이고 이전에 비가 내리지 않은 칸에서 구름 생성 후 옮기기
                if arr[r][c] >= 2 and visited[r][c] != cnt - 1:
                    arr[r][c] -= 2
                    clouds.append([(r + dir[d][0] * s) % N, (c + dir[d][1] * s) % N])

    # 구름이 다 옮겨졌으면 비 내리고 visited 추가, 물복사버그 마법 시전
    for r, c in clouds:
        arr[r][c] += 1
        visited[r][c] = cnt
    # 물복사버그 마법 시전
    for r, c in clouds:
        for d in dir_x:
            nr, nc = r + d[0], c + d[1]
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] > 0:
                arr[r][c] += 1
    # print(clouds)
    # print(arr)



N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# M번 만큼 구름 이동
cnt = 0
# 비가 내렸던 곳 판단
visited = [[0] * N for _ in range(N)]
for _ in range(M):
    cnt += 1
    d, s = map(int, input().split())
    move_cloud(d, s)

# 마지막에도 구름이 생겨야하므로
sum_water = 0
for r in range(N):
    for c in range(N):
        # 물이 2 이상이고 이전에 비가 내리지 않은 칸에서 구름 생성 후 옮기기
        if arr[r][c] >= 2 and visited[r][c] != cnt:
            arr[r][c] -= 2
        sum_water += arr[r][c]

print(sum_water)
