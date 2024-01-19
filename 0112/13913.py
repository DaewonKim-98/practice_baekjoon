import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
visited = [0] * 100001
# index가 왔던 경로를 나타내는 path 배열
path = [0] * (100001)

# 최단거리를 찾는 bfs
def bfs(N, K):
    visited[N] = 1
    q = deque()
    q.append(N)

    while len(q) > 0:
        t = q.popleft()
        # 동생의 위치로 이동하면
        if t == K:
            return
        # 수빈이가 움직일 수 있는 위치들을 리스트화
        t_list = [t - 1, t + 1, 2 * t]
        # 수빈이가 움직인 곳에서 방문하지 않은 곳이라면
        for x in t_list:
            # 배열의 범위를 벗어나면 안되므로
            if 0 <= x < 100001:
                # 방문하지 않았으면
                if visited[x] == 0:
                    q.append(x)
                    visited[x] = visited[t] + 1
                    path[x] = t

# print(bfs(N, K))
# print(visited[:20])
bfs(N, K)
print(visited[K] - 1)
# K에서 다시 N으로 갈 때까지 path를 돌면서 출력
how = []
while K != N:
    how.append(K)
    K = path[K]

print(N, end=' ')
for i in range(len(how) - 1, -1, -1):
    print(how[i], end=' ')

