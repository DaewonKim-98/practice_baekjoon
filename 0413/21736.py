from collections import deque

dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def bfs(r, c):
    visited = [[0] * M for _ in range(N)]
    q = deque()
    visited[r][c] = 1
    q.append((r, c))
    cnt = 0
    
    while q:
        r, c = q.popleft()
        if arr[r][c] == 'P':
            cnt += 1
        
        for d in dir:
            nr, nc = r + d[0], c + d[1]
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and arr[nr][nc] != 'X':
                q.append((nr, nc))
                visited[nr][nc] = 1
    
    if cnt == 0:
        print('TT')
    else:          
        print(cnt)
    

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

# I에서 시작해서 bfs
for r in range(N):
    for c in range(M):
        if arr[r][c] == 'I':
            bfs(r, c)
            exit()