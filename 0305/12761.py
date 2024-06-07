from collections import deque

def bfs(N):
  q = deque()
  q.append((N, 0))
  visited[N] = 1
  
  while q:
    i, cnt = q.popleft()
    # 도착하면
    if i == M:
      print(cnt)
      return
    
    for ni in [i + 1, i - 1, i + A, i - A, i + B, i - B, i * A, i * B]:
      # 범위를 안벗어나고 방문하지 않았으면
      if 0 <= ni <= 100000 and visited[ni] == 0:
        q.append((ni, cnt + 1))
        visited[ni] = 1


A, B, N, M = map(int, input().split())

# bfs를 통해
visited = [0] * 100001
bfs(N)