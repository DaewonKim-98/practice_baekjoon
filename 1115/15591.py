from collections import deque
def bfs(v):
    global cnt
    visited = [0] * (N + 1)
    q = deque()
    visited[v] = 1000000000
    # 처음 visited[v]는 v랑 연결된 것들 중에서 k보다 크거나 같으면서 가장 작은 것으로
    for i in arr[v]:
        if i[0] >= k:
            visited[v] = min(visited[v], i[0])
    q.append(v)

    while q:
        p = q.popleft()
        for i in arr[p]:
            # 방문하지 않았고 최소가 k보다 크거나 같은 것들
            if visited[i[1]] == 0 and min(i[0], visited[p]) >= k:
                q.append(i[1])
                visited[i[1]] = min(i[0], visited[p])
                cnt += 1


N, Q = map(int, input().split())
# 간선과 각 사이의 유사도
arr = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    p, q, r = map(int, input().split())
    arr[p].append([r, q])
    arr[q].append([r, p])

for _ in range(Q):
    cnt = 0
    k, v = map(int, input().split())
    # v에 대해 bfs를 통해 길이가 짧은 것들 제거
    bfs(v)
    print(cnt)