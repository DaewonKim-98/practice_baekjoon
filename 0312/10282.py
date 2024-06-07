import heapq

def bfs(c):
  visited = [0] * (N + 1)
  q = []
  heapq.heappush(q, (0, c))
  allTime = 0
  
  while q:
    time, c = heapq.heappop(q)
    if visited[c] == 0:
      visited[c] = 1
      allTime = time
      for i in dependence[c]:
        if visited[i[0]] == 0:
          heapq.heappush(q, (time + i[1], i[0]))
  cnt = 0
  for i in range(N + 1):
    if visited[i] == 1:
      cnt += 1
  print(cnt, allTime)

T = int(input())
for case in range(1, T + 1):
  N, D, C = map(int, input().split())
  dependence = [set() for _ in range(N + 1)]
  for _ in range(D):
    a, b, s = map(int, input().split())
    dependence[b].add((a, s))
    
  # bfs를 통해 다이스트라
  bfs(C)