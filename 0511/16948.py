from collections import deque

def bfs(r, c):
    q = deque()
    visited = [[0] * N for _ in range(N)]
    q.append((r, c))
    visited[r][c] = 1
    
    while q:
        r, c = q.popleft()
        if r == r2 and c == c2:
            print(visited[r][c] - 1)
            return
        for d in dir:
            nr, nc = r + d[0], c + d[1]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                visited[nr][nc] = visited[r][c] + 1
                q.append((nr, nc))
                
    # 다 돌아도 없으면
    print(-1)
    return

N = int(input())
r1, c1, r2, c2 = map(int, input().split())

# bfs로
arr = [[0] * N for _ in range(N)]
dir = [[-2, -1], [-2, 1], [0, -2], [0, 2], [2, -1], [2, 1]]

bfs(r1, c1)