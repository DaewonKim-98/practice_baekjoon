N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]

# 이동할 방향 표시
dir = [[0, -1], [-1, 0], [0, 1], [1, 0]]

# bfs로 미로 통과
def bfs(N, M):
    visited = [[0] * (M) for _ in range(N)]
    # 인덱스는 0, 0부터 시작
    visited[0][0]= 1
    q = []
    q.append([0, 0])
    
    while len(q) > 0:
        [r, c] = q.pop(0)
        for d in dir:
            nr ,nc = r + d[0], c + d[1]
            # 배열 안에 있고 방문하지 않았으면
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0:
                # 갈 수 있는 길이면
                if arr[nr][nc] != 0:
                    # q에 추가하고 1을 추가해서 방문했다는 표시
                    q.append([nr, nc])
                    visited[nr][nc] = visited[r][c] + 1
    # 인덱스이므로 N - 1, M - 1까지
    return visited[N - 1][M - 1]

print(bfs(N, M))