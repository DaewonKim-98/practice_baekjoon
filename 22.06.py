from collections import deque

dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def move(r, c):
    q = deque()
    q.append((r, c, False))
    visited = [[1000000] * M for _ in range(N)]
    brokeVisited = [[1000000] * M for _ in range(N)]
    visited[0][0] = 1
    
    while q:
        r, c, broke = q.popleft()
        if r == N - 1 and c == M - 1:
            return min(visited[r][c], brokeVisited[r][c])
        for d in dir:
            nr, nc = r + d[0], c + d[1]
            # 벽을 부순 상태면 부수지 않고 이동
            if broke == True:
                if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0 and brokeVisited[nr][nc] == 1000000:
                    brokeVisited[nr][nc] = brokeVisited[r][c] + 1
                    q.append((nr, nc, broke))
            else:
                # 벽 부수지 않고 이동
                if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0 and visited[nr][nc] == 1000000:
                    visited[nr][nc] = visited[r][c] + 1
                    q.append((nr, nc, broke))
                    
                # 벽 부수고 이동
                elif 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 1 and brokeVisited[nr][nc] == 1000000:
                    brokeVisited[nr][nc] = min(visited[r][c] + 1, brokeVisited[nr][nc])
                    q.append((nr, nc, True))
    
    return -1
    
N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

result = move(0, 0)
print(result)