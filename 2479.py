import sys
from collections import deque
input = sys.stdin.readline

def findRoute(a, b):
  q = deque()
  q.append((a, [a]))
  visited = [0] * (N + 1)
  visited[a] = 1

  while q:
    num, route = q.popleft()
    if num == b:
      for i in route:
        print(i, end=' ')
      return
    
    for next in hdic[num]:
      if visited[next] == 0:
        visited[next] = 1
        q.append((next, route + [next]))
  
  # 경로가 존재하지 않으면
  print(-1)
  return

N, K = map(int, input().strip().split())
codes = list(list(map(int, input().strip())) for _ in range(N))
codes = [0] + codes
A, B = map(int, input().strip().split())

hdic = {}
for i in range(1, N + 1):
  hdic[i] = []
for i in range(1, N):
  for j in range(i + 1, N + 1):
    cnt = 0
    for k in range(K):
      if codes[i][k] != codes[j][k]:
        cnt += 1
    # 다른게 하나면
    if cnt == 1:
      hdic[i].append(j)
      hdic[j].append(i)

# bfs로 경로 찾기
findRoute(A, B)