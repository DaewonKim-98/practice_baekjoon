from collections import deque

dir = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]

def findWord(r, c):
    visited[r][c] = 1
    q = deque([])
    q.append((r, c))
    
    while q:
        r, c = q.popleft()
        for d in dir:
            nr, nc = r + d[0], c + d[1]
            if 0 <= nr < M and 0 <= nc < N and arr[nr][nc] == 1 and visited[nr][nc] == 0:
                q.append((nr, nc))
                visited[nr][nc] = 1

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]

cnt = 0
visited = [[0] * N for _ in range(M)]
for r in range(M):
    for c in range(N):
        if arr[r][c] == 1 and visited[r][c] == 0:
            cnt += 1
            findWord(r, c)
            
print(cnt)