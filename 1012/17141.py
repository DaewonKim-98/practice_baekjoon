def make_com(i, l):
    if i == M:
        virus_location.append(p[:])
        return
    for j in range(len(virus_location_list)):
        if j >= l:
            if visited[j] == 0:
                p[i] = j
                visited[j] = 1
                make_com(i + 1, j)
                visited[j] = 0

# 방향
dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def bfs(virus):
    global min_time
    q = []
    for i in virus:
        # q에 바이러스의 위치들 추가, 방문 표시
        q.append(virus_location_list[i])
        bfs_visited[virus_location_list[i][0]][virus_location_list[i][1]] = 1

    last_r, last_c = 0, 0
    while q:
        r, c = q.pop(0)
        last_r , last_c = r, c
        for d in dir:
            nr, nc = r + d[0], c + d[1]
            if 0 <= nr < N and 0 <= nc < N and bfs_visited[nr][nc] == 0:
                q.append([nr, nc])
                bfs_visited[nr][nc] = bfs_visited[r][c] + 1

    # while문이 끝나고 다 돌렸을 때 0이 남아있으면 모든 빈칸에 바이러스를 퍼뜨릴 수 없으므로
    can_spread = True
    for r in range(N):
        for c in range(N):
            if bfs_visited[r][c] == 0:
                can_spread = False
                break
    
    # 퍼뜨릴 수 있으면 마지막 방문 값 -1이 퍼뜨릴 수 있는 시간
    if can_spread == True:
        if min_time > bfs_visited[last_r][last_c] - 1:
            min_time = bfs_visited[last_r][last_c] - 1


import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 바이러스를 퍼뜨릴 수 있는 자리 리스트
virus_location_list = []
for r in range(N):
    for c in range(N):
        if arr[r][c] == 2:
            virus_location_list.append([r, c])

# 자리 조합으로 만들기
i = 0
p = [0] * M
num = list(range(len(virus_location_list)))
visited = [0] * len(virus_location_list)

# 바이러스 자리들
virus_location = []
make_com(i, 0)

# bfs를 돌리면서 바이러스가 퍼지는 시간 계산
min_time = 10000000000
for virus in virus_location:
    bfs_visited = [[0] * N for _ in range(N)]
    # visited에 벽 표시
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 1:
                bfs_visited[r][c] = -1
    bfs(virus)
    
if min_time == 10000000000:
    min_time = -1
print(min_time)