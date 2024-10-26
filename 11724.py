import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(i):
  for j in link[i]:
    if visited[j] == 0:
      visited[j] = 1
      dfs(j)

N, M = map(int, input().strip().split())
link = [[] for _ in range(N + 1)]
for _ in range(M):
  u, v = map(int, input().strip().split())
  link[u].append(v)
  link[v].append(u)

visited = [0] * (N + 1)
cnt = 0
for i in range(1, N + 1):
  if visited[i] == 0:
    cnt += 1
    dfs(i)

print(cnt)