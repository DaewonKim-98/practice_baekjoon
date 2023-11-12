# 방향
dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

# 그람 없이 가는 것
def bfs(r, c):
    global min_time
    visited = [[0] * (M) for _ in range(N)]
    q = []
    visited[r][c] = 1
    q.append((r, c))

    while q:
        r, c = q.pop(0)
        if r == N - 1 and c == M - 1:
            min_time = min(min_time, visited[r][c] - 1)
        for d in dir:
            nr, nc = r + d[0], c + d[1]
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and arr[nr][nc] != 1:
                q.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1
                
# 그람을 찾아서 가는 것
def bfs_gram(r, c):
    global min_time
    visited = [[0] * (M) for _ in range(N)]
    q = []
    visited[r][c] = 1
    q.append((r, c))
    gram = ()

    while q:
        r, c = q.pop(0)
        # 그람을 찾았으면
        if arr[r][c] == 2:
            gram = (r, c)
            break
        for d in dir:
            nr, nc = r + d[0], c + d[1]
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and arr[nr][nc] != 1:
                q.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1
    
    # 벽 상관없이 그냥 갈 수 있으므로
    if gram:
        r, c = gram
        to_gram = visited[r][c] - 1
        min_time = min(min_time, to_gram + N - 1 - r + M - 1 - c)
                

N, M, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# bfs를 통해 시간을 구하는데 그람을 만났을 때에도 구해서 최솟값 구하기
r, c = 0, 0
min_time = 10001
bfs(r, c)
bfs_gram(r, c)

if min_time > 10000 or min_time > T:
    print('Fail')
else:
    print(min_time)