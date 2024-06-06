def dfs(i, cnt):
  if cnt == 5:
    print(1)
    exit()

  for j in link[i]:
    if visited[j] == 0:
      visited[j] = 1
      dfs(j, cnt + 1)
      visited[j] = 0

N, M = map(int, input().split())
link = [[] for _ in range(N)]
for _ in range(M):
  a, b = map(int, input().split())
  link[a].append(b)
  link[b].append(a)
  
# 5개의 연속된 연결이 있는지
for i in range(N):
  visited = [0] * N
  visited[i] = 1
  dfs(i, 1)
  
print(0)