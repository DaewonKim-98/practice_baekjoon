def bfs(i):
    visited = [0] * (N + 1)
    q = []
    visited[i] = 1
    q.append(i)

    while q:
        p = q.pop()
        for j, d in n_list[p]:
            if visited[j] == 0:
                q.append(j)
                visited[j] = visited[p] + d

    # while문이 끝나고 visited의 최댓값이 그 거리
    return (visited.index(max(visited)), max(visited) - 1)


N = int(input())
n_list = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    # 간선과 그 거리 추가
    a, b, d = map(int, input().split())
    n_list[a].append((b, d))
    n_list[b].append((a, d))

# bfs를 통해 어떤 한 노드에서 가장 큰 거리를 구한다음 그 노드에서 다시 가장 멀리 있는 노드까지의
# 거리가 이 노드의 지름
# 모든 노드는 지름의 안에 있기 때문

# 가장 쉽게 1로 계산
i = 1
print(bfs(bfs(i)[0])[1])