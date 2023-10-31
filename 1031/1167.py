def bfs(i):
    visited = [0] * (V + 1)
    q = []
    visited[i] = 1
    q.append(i)

    while q:
        p = q.pop()
        for j in arr[p]:
            # 방문하지 않은 곳이면
            if visited[j[0]] == 0:
                q.append(j[0])
                visited[j[0]] = visited[p] + j[1]
    return (max(visited), visited.index(max(visited)))

V = int(input())
arr = [[] for _ in range(V + 1)]
for i in range(V):
    lst = list(map(int, input().split()))
    j = 1
    while lst[j] != -1:
        arr[lst[0]].append((lst[j], lst[j + 1]))
        j += 2
    
# 한 점에서 그냥 시작해서 가장 먼 곳 찾고 다음 그 점에서 가장 먼 곳까지의 거리 찾으면 지름
i = 1
print(bfs(bfs(i)[1])[0] - 1)