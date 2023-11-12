def bfs(a):
    visited = [0] * (N + 1)
    q = []
    visited[a] = 1
    q.append(a)

    while q:
        p = q.pop()

        # b를 찾으면 b까지의 거리 출력
        if p == b:
            print(visited[p] - 1)
            return
        
        # 연결된 노드 중에서
        for i in n_list[p]:
            # 방문하지 않았으면
            if visited[i[0]] == 0:
                q.append(i[0])
                visited[i[0]] = visited[p] + i[1]

                
N, M = map(int, input().split())
n_list = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b, d = map(int, input().split())
    n_list[a].append((b, d))
    n_list[b].append((a, d))
    
# bfs를 통해 거리 찾기
for _ in range(M):
    a, b = map(int, input().split())
    bfs(a)