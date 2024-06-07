import sys
import heapq
input = sys.stdin.readline

def bfs(i):
  q = []
  heapq.heapify(q)
  visited = [0] * (N + 1)
  heapq.heappush(q, (0, 1))
  allCost = 0
  maxCost = 0
  cnt = 0
  
  while q:
    cost, i = heapq.heappop(q)
    if visited[i] == 0:
      cnt += 1
      allCost += cost
      maxCost = max(maxCost, cost)
      visited[i] = 1
      
      for j in link[i]:
        heapq.heappush(q, (j[0], j[1]))
  
  # 다 끝나면 다이스트라로 연결이 모두 끝났다는 것이므로
  # print(maxCost)
  # print(allCost)
  print(allCost - maxCost)
        

N, M = map(int, input().strip().split())
link = [[] for _ in range(N + 1)]

for _ in range(M):
  a, b, c = map(int, input().strip().split())
  link[a].append((c, b))
  link[b].append((c, a))
  
# 가장 끝에서 끝까지 최소로 갈 수 있는 것을 찾고
# 사이에서 가장 큰 유지비를 빼면 그게 두 마을의 최소 유지비

# 다이스트라로 모두를 연결하는 최소 유지비 찾기
bfs(1)