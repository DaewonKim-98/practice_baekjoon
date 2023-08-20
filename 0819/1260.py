import sys
input = sys.stdin.readline

dfs_visit = []
def dfs(e_list, N, V):
    visited = [0] * (N + 1)
    visited[V] = 1
    stack = []
    dfs_visit.append(V)
    while True:
        # 정점이 작은 것부터 방문이므로
        e_list[V].sort()
        for w in e_list[V]:
            # 방문하지 않았다면
            if visited[w] == 0:
                stack.append(V)
                V = w
                visited[V] = 1
                # 순서를 알기 위해 추가
                dfs_visit.append(V)                
                break
        else:
            if stack:
                V = stack.pop()
            else:
                break

            
bfs_visit = []
def bfs(e_list, N, V):
    visited = [0] * (N + 1)
    visited[V] = 1
    q = []
    q.append(V)
    
    # 큐에 원소가 있는 동안
    while len(q) > 0:
        t = q.pop(0)
        bfs_visit.append(t)
        # 정점이 작은 것부터 방문이므로
        e_list[t].sort()
        for w in e_list[t]:
            # 방문하지 않으면
            if visited[w] == 0:
                # q에 쌓고
                q.append(w)
                # 방문했다고 표시
                visited[w] = 1
                
    
                


N, M, V = map(int, input().split())
e_list = [[] for _ in range(N + 1)]
# 간선 리스트에 표시
for e in range(M):
    a, b = map(int, input().split())
    e_list[a].append(b)
    e_list[b].append(a)

dfs(e_list, N, V)
bfs(e_list, N, V)
print(*dfs_visit)
print(*bfs_visit)