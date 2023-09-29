R, C, K = map(int, input().split())
arr = [list(input()) for _ in range(R)]

# 방향과 방문 표시
dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
visited = [[0] * C for _ in range(R)]

# 캠프 위치
r, c = R - 1, 0
cnt = 0
visited[r][c] = 1
# 방문지점까지 탐색
def dfs(r, c):
    global cnt
    # 거리가 K이고
    if visited[r][c] == K:
        # 집까지 가면
        if r == 0 and c ==  C - 1:
            cnt += 1
        return
    
    
    # 방향에 따라 재귀로 탐색
    for d in dir:
        nr, nc = r + d[0], c + d[1]
        if 0 <= nr < R and 0 <= nc < C and visited[nr][nc] == 0 and arr[nr][nc] != 'T':
            visited[nr][nc] = visited[r][c] + 1
            dfs(nr, nc)
            visited[nr][nc] = 0

dfs(r, c)       
print(cnt)