# 방향
dir = [[-1, 0], [0, -1], [0, 1], [1, 0]]

# 물고기를 먹는 bfs
def bfs(r, c):
    global shark_size
    global eat_fish
    global time
    q = []
    visited[r][c] = 1
    q.append([visited[r][c], r, c])

    while q:
        # 가장 위에, 가장 왼쪽에 있는 물고기를 출력해야 하므로 정렬
        q.sort()
        v, r, c = q.pop(0)
        # 만약 자기보다 작은 물고기에 도착했으면 먹으므로
        if 0 < arr[r][c] < shark_size:
            arr[r][c] = 0
            eat_fish += 1
            # 먹은 물고기가 상어 크기만큼 된다면 상어 크기도 올려줘야 하므로
            if eat_fish == shark_size:
                shark_size += 1
                eat_fish = 0
            time += v - 1
            return (r, c)
        for d in dir:
            nr, nc = r + d[0], c + d[1]
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] <= shark_size and visited[nr][nc] == 0:
                visited[nr][nc] = v + 1
                q.append([visited[nr][nc], nr, nc])
    # 만약 현재 위치에서 가지 못하는 경우면
    return -1, -1
                


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 아기 상어 크기와 먹은 물고기 수
shark_size = 2
eat_fish = 0

# 아기 상어 자리 찾기
r, c = 0, 0
for x in range(N):
    for y in range(N):
        if arr[x][y] == 9:
            r, c = x, y
            break
arr[r][c] = 0
# 상어가 더 이상 먹을게 없을 때까지 반복
time = 0
while True:
    # 처음에는 상어는 더 이상 먹을게 없다고 생각
    can_eat = False

    visited = [[0] * N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            # 먹을게 있다면
            if 0 < arr[x][y] < shark_size:
                can_eat = True
                break
        if can_eat == True:
            break
    # 먹을게 없으면 while문 종료
    if can_eat == False:
        break
    
    # print(arr)
    # print(r, c, shark_size, time)
    # 먹을게 있으면 bfs로 먹을거 탐색 / r, c 다시 갱신
    r, c = bfs(r, c)
    if r == -1 and c == -1:
        break

print(time)