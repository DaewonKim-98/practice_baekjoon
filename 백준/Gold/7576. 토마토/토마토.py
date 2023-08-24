import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

# 토마토를 익게 하는 bfs
def bfs(ripe_list):
    # 상하좌우 방향을 나타낼 dir
    d = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    # 큐
    q = deque()    
    for [r, c] in ripe_list:
        q.append([r, c])
    
    a, b = 0, 0
    while len(q) > 0:
        [r, c] = q.popleft()
        a, b = r, c
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if (0 <= nr < N) and (0 <= nc < M) and (arr[nr][nc] == 0):
                q.append([nr, nc])
                arr[nr][nc] = arr[r][c] + 1

    # 다 끝나고 나면 마지막 q에 있는 visited의 값을 출력하는데 그것이 모두 익을 때까지의 날짜
    return arr[a][b] - 1

ripe_list = []
for r in range(N):
    for c in range(M):
        if arr[r][c] == 1:
            ripe_list.append([r, c])

day = bfs(ripe_list)
# 다 돌렸을 때에도 0이 남아있다면 모두 익지 못하므로
result = True
for r in range(N):
    for c in range(M):
        if arr[r][c] == 0:
            result = False

if result == False:
    print(-1)
else:
    print(day)
