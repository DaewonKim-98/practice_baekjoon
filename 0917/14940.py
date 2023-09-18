import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 방향
dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def bfs(r, c):
    visited[r][c] = 0
    q = []
    q.append([r, c])
    
    while len(q) > 0:
        [r, c] = q.pop(0)
        for d in dir:
            nr, nc = r + d[0], c + d[1]
            if 0 <= nr < n and 0 <= nc < m and visited[nr][nc] == -1 and visited[nr][nc] != 0:
                visited[nr][nc] = visited[r][c] + 1
                q.append([nr, nc])
            
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# visited
visited = [[-1] * m for _ in range(n)]

x, y = 0, 0
# 목표지점 2
for r in range(n):
    for c in range(m):
        if arr[r][c] == 2:
            x, y = r, c
        elif arr[r][c] == 0:
            visited[r][c] = 0
            
bfs(x, y)
for r in range(n):
    for c in range(m):
        print(visited[r][c], end=' ')
    print()