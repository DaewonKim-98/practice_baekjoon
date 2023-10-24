def dfs(i, n, l):
    if i == n:
        second = []
        for num in numbers:
            if num not in first:
                second.append(num)
        if [second, first[:]] not in election_ward:
            election_ward.append([first[:], second])
        return
    for j in range(l, N + 1):
        if visited[j] == 0:
            first.append(j)
            visited[j] = 1
            dfs(i + 1, n, j)
            first.pop()
            visited[j] = 0

def bfs(i):
    visited_bfs = [0] * (N + 1)
    q = []
    visited_bfs[i] = populations[i]
    q.append(i)

    while q:
        p = q.pop()
        for j in E_list[p]:
            if visited_bfs[j] == 0 and j in w:
                q.append(j)
                visited_bfs[j] = populations[j]

    connect = True
    for k in w:
        if visited_bfs[k] == 0:
            connect = False
            break
    return connect

N = int(input())
populations = [0] + list(map(int, input().split()))
# 인접 리스트를 나타내는 리스트
E_list = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    arr = list(map(int, input().split()))
    for j in range(1, arr[0] + 1):
        E_list[i].append(arr[j])

# N개 구역을 두개의 선거구로 나누는 dfs
numbers = list(range(1, N + 1))
i = 0
visited = [0] * (N + 1)
first = []
election_ward = []
for n in range(1, N // 2 + 1):
    dfs(i, n, 1)

min_sub = 1000
# 두개의 선거 구역 리스트를 돌면서 하나의 점에서 시작하는 bfs를 통해 각각이 연결되어 있는지 확인하고
for ward in election_ward:
    w = ward[0][:]
    if not bfs(w[0]):
        continue
    w = ward[1][:]
    if not bfs(w[0]):
        continue

    # 각각이 연결되어 있다면 각 선거구 인구의 합
    sum1 = 0
    for i in ward[0]:
        sum1 += populations[i]
    sum2 = 0
    for i in ward[1]:
        sum2 += populations[i]
    min_sub = min(min_sub, abs(sum1 - sum2))
    
if min_sub == 1000:
    min_sub = -1

print(min_sub)