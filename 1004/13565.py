M, N = map(int, input().split())
arr = [list(map(int, input())) for _ in range(M)]

# bfs를 통해 길찾기
# 방향
dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
visited = [[0] * N for _ in range(M)]
result = 'NO'

# bfs
def bfs(r, c):
    global result
    q = []
    q.append([r, c])
    visited[r][c] = 1

    # for문을 돌면서 찾기
    while q:
        r, c = q.pop(0)
        # r이 마지막 줄인 M - 1에 도달하면 그만
        if r == M - 1:
            result = 'YES'
            return
        for d in dir:
            nr, nc = r + d[0], c + d[1]
            if 0 <= nr < M and 0 <= nc < N and arr[nr][nc] == 0 and visited[nr][nc] == 0:
                q.append([nr, nc])
                visited[nr][nc] = 1

# 첫째줄에서 0인 부분을 찾아 bfs
for c in range(N):
    if arr[0][c] == 0:
        bfs(0, c)
        if result == 'YES':
            break

print(result)