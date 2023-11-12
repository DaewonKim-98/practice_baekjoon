dir = [[0, 1], [1, 0], [-1, 0], [0, -1]]

def dfs(r, c, cnt):
    global cycle
    visited[r][c] = 1
    
    for d in dir:
        nr, nc = r + d[0], c + d[1]
        # 다시 시작점으로 돌아간다면 사이클이 존재한다는 것이므로
        if nr == first[0] and nc == first[1] and cnt >= 4:
            cycle = True
            return
        if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and arr[nr][nc] == first[2]:
            # print(visited)
            dfs(nr, nc, cnt + 1)
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

# dfs를 통해 쭉 연결했을 때 다시 자신으로 돌아온다면 사이클
cycle = False
for r in range(N):
    for c in range(M):
        visited = [[0] * M for _ in range(N)]
        # 시작점
        first = (r, c, arr[r][c])
        # 재귀를 돌 때 4개의 점 이상으로 이어졌을 때 사이클이므로 cnt도 함께 봐주기
        cnt = 1
        dfs(r, c, cnt)
        if cycle == True:
            print('Yes')
            exit()

# 다 돌았는데도 사이클이 아니면
print('No')