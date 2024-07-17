from collections import deque

dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def makeBridge(r, c):
    global minLength
    q = deque()
    q.append((r, c))
    visited[r][c] = 1
    # 바다랑 닿아 있는 부분
    closeSea = set()
    sea = set()
    seaVisited = [[0] * N for _ in range(N)]
    
    while q:
        a, b = q.popleft()
        for d in dir:
            nr, nc = a + d[0], b + d[1]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                # 대륙이면 그냥 q에 넣기
                if arr[nr][nc] == 1:
                    q.append((nr, nc))
                    visited[nr][nc] = 1
                # 바다면
                else:
                    closeSea.add((a, b))
                    sea.add((nr, nc))
                    seaVisited[nr][nc] = 1
    # print(sea)
    # print(closeSea)
    # print(seaVisited)
    # 바다에서 다른 대륙 찾기
    sea = deque(sea)
    
    while sea:
        a, b = sea.popleft()
        # 다리가 이미 있는 다리보다 길면 컷
        if seaVisited[a][b] - 1 >= minLength:
            continue
        # 다른 대륙에 도착했으면
        if arr[a][b] == 1:
            minLength = min(seaVisited[a][b] - 1, minLength)
        for d in dir:
            nr, nc = a + d[0], b + d[1]
            if 0 <= nr < N and 0 <= nc < N and seaVisited[nr][nc] == 0 and (nr, nc) not in closeSea:
                sea.append((nr, nc))
                seaVisited[nr][nc] = seaVisited[a][b] + 1
    # print(seaVisited)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 바다랑 맞닿아 있는 부분에서 bfs를 통해 가장 짧은 다리 찾기
visited = [[0] * N for _ in range(N)]
minLength = 1000
for r in range(N):
    for c in range(N):
        if visited[r][c] == 0 and arr[r][c] == 1:
            makeBridge(r, c)
            
print(minLength)