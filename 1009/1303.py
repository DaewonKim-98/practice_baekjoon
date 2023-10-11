# 방향
dir = [[0, 1], [1, 0], [-1, 0], [0, -1]]

# 탐색
def bfs(r, c):
    global white
    global blue
    cnt = 0
    q = []
    visited[r][c] = 1
    q.append([r, c])
    
    while q:
        r, c = q.pop(0)
        cnt += 1
        for d in dir:
            nr, nc = r + d[0], c + d[1]
            if 0 <= nr < M and 0 <= nc < N and visited[nr][nc] == 0:
                # W인지 B인지 구분
                if arr[r][c] == 'W' and arr[nr][nc] == 'W':
                    q.append([nr, nc])
                    visited[nr][nc] = 1
                elif arr[r][c] == 'B' and arr[nr][nc] == 'B':
                    q.append([nr, nc])
                    visited[nr][nc] = 1
                    
    if arr[r][c] == 'W':
        white += cnt ** 2
    else:
        blue += cnt ** 2
        
N, M = map(int, input().split())
arr = [list(input()) for _ in range(M)]

# bfs를 통해 뭉쳐있는 아군의 수와 적군의 수를 찾고 제곱해서 각각 더하기
white = 0
blue = 0
visited = [[0] * N for _ in range(M)]

for r in range(M):
    for c in range(N):
        if visited[r][c] == 0:
            bfs(r, c)
          
print(white, blue)