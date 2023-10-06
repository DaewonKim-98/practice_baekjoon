# 1 찾을 bfs
def bfs(r, c):
    global max_garage
    garage = 0
    q = []
    q.append([r, c])
    visited[r][c] = 1

    while q:
        r, c = q.pop(0)
        # 연결된 음식물 쓰레기의 최댓값 갱신
        garage += 1
        max_garage = max(max_garage, garage)
        for d in dir:
            nr, nc = r + d[0], c + d[1]
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 1 and visited[nr][nc] == 0:
                q.append([nr, nc])
                visited[nr][nc] = 1


N, M, K = map(int, input().split())
arr = [[0] * M for _ in range(N)]
for _ in range(1, K + 1):
    r, c = map(int, input().split())
    arr[r - 1][c - 1] = 1

# 방향
dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

# arr을 돌면서 1 찾기
# bfs를 통해
visited = [[0] * M for _ in range(N)]
max_garage = 0
for r in range(N):
    for c in range(M):
        # 쓰레기더미이고 방문하지 않았으면
        if arr[r][c] != 0 and visited[r][c] == 0:
            bfs(r, c)


print(max_garage)