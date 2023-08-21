import sys
input = sys.stdin.readline

N, K = map(int, input().split())

# 최단거리를 찾는 bfs
def bfs(N, K):
    visited = [0] * 100001
    visited[N] = 1
    q = [N]

    while len(q) > 0:
        t = q.pop(0)
        # 동생의 위치로 이동하면
        if t == K:
            return visited[t] - 1
        # 수빈이가 움직일 수 있는 위치들을 리스트화
        t_list = [t - 1, t + 1, 2 * t]
        # 수빈이가 움직인 곳에서 방문하지 않은 곳이라면
        for x in t_list:
            # 배열의 범위를 벗어나면 안되므로
            if 0 <= x < 100001:
                if visited[x] == 0:
                    q.append(x)
                    visited[x] = visited[t] + 1

print(bfs(N, K))