from collections import deque

def bfs(q):
    visited = [0] * (N + 1)
    que = deque()
    for i in q:
        que.append(i)
        visited[i] = 2
    visited[1] = 1

    while que:
        p = que.popleft()
        if p == N:
            print(visited[p])
            return
        for lst in arr:
            # p가 집합안에 있으면 다 연결가능한 곳이므로
            if p in lst:
                for i in lst:
                    if visited[i] == 0:
                        que.append(i)
                        visited[i] = visited[p] + 1
                arr.remove(lst)

    # 다 돌아도 갈 수 없으면
    print(-1)
    return


N, K, M = map(int, input().split())
if N == 1:
    print(1)
    exit()

arr = []
# 1과 연결된 q
q = deque()
for _ in range(M):
    lst = set(map(int, input().split()))
    if 1 in lst:
        lst.remove(1)
        q.extend(lst)
    else:
        arr.append(lst)
if not q:
    print(-1)
    exit()

bfs(q)