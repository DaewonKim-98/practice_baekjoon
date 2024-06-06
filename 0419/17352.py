import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(i):
  for j in link[i]:
    if visited[j] == 0:
      visited[j] = 1
      dfs(j)

N = int(input().strip())
link = [[] for _ in range(N + 1)]

if N == 2:
  print(1, 2)
  exit()

for _ in range(N - 2):
  a, b = map(int, input().strip().split())
  link[a].append(b)
  link[b].append(a)
  
# 쭉 연결해서 연결 안된 것이 있으면 그냥 연결
visited = [0] * (N + 1)
for i in range(1, N + 1):
  if len(link[i]) > 0:
    visited[i] = 1
    dfs(i)
    # 돌면서 방문 안한 곳과 연결
    for j in range(1, N + 1):
      if visited[j] == 0:
        print(i, j)
        exit()