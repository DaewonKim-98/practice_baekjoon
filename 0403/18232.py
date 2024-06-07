from collections import deque

def bfs(s):
  q = deque()
  visited = [0] * N
  q.append(s)
  visited[s] = 1
  
  while q:
    s = q.popleft()
    # 도착하면
    if s == E:
      print(visited[s] - 1)
      return
    
    for i in teleport[s]:
      if visited[i] == 0:
        q.append(i)
        visited[i] = visited[s] + 1
        
    for i in [s + 1, s - 1]:
      if 0 <= i < N and visited[i] == 0:
        q.append(i)
        visited[i] = visited[s] + 1

N, M = map(int, input().split())
S, E = map(int, input().split())
teleport = [[] for _ in range(N)]
for _ in range(M):
  x, y = map(int, input().split())
  teleport[x - 1].append(y - 1)
  teleport[y - 1].append(x - 1)
  
# print(teleport)
S -= 1
E -= 1

# bfs를 통해 최소 시간 출력
bfs(S)