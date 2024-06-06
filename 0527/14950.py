import sys
import heapq
input = sys.stdin.readline

def getMinCost(i):
  q = []
  visited = [0] * (N + 1)
  heapq.heappush(q, (0, 1))
  minCost = 0
  
  while q:
    cost, i = heapq.heappop(q)
    if visited[i] == 0:
      minCost += cost
      visited[i] = 1
      for j in link[i]:
        heapq.heappush(q, (j[0], j[1]))
  # print(minCost)
  minCost += T * ((N - 1) * (N - 2) // 2)
  print(minCost)

N, M, T = map(int, input().strip().split())
link = [[] for _ in range(N + 1)]
for _ in range(M):
  a, b, c = map(int, input().strip().split())
  link[a].append((c, b))
  link[b].append((c, a))

# 다이스트라
getMinCost(1)