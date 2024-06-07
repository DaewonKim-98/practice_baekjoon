from collections import deque

def bfs(a):
  q = deque()
  visited = [0] * (N + 1)
  q.append(a)
  visited[a] = 1
  
  while q:
    a = q.popleft()
    if a == B:
      print(visited[a] - 1)
      return
    
    for i in link[a]:
      if visited[i] == 0:
        q.append(i)
        visited[i] = visited[a] + 1
        
  # 끝까지 가도 불가능이면
  print(-1)
  return

A, B = map(int, input().split())
N, M = map(int, input().split())
link = [[] for _ in range(N + 1)]
for _ in range(M):
  x, y = map(int, input().split())
  link[x].append(y)
  link[y].append(x)
  
# bfs를 통해
bfs(A)