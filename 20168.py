import sys
import heapq
input = sys.stdin.readline

def start(A):
  q = []
  visited = [0] * (N + 1)
  heapq.heappush(q, (0, A, 0, 0))
  
  while q:
    amount, i, maxAmount, totalAmount = heapq.heappop(q)
    
    if visited[i] == 0:
      visited[i] = 1
      
      # 도착하면
      if i == B:
        print(maxAmount)
        return
      
      # 연결
      for j in link[i]:
        if visited[j[1]] == 0:
          # 갈 수 있으면
          if totalAmount + j[0] <= C:
            heapq.heappush(q, (j[0], j[1], max(maxAmount, j[0]), totalAmount + j[0]))
      
  # 도착할 수 없으면
  print(-1)
  return

N, M, A, B, C = map(int, input().strip().split())
link = [[] for _ in range(N + 1)]
for _ in range(M):
  a, b, c = map(int, input().strip().split())
  link[a].append((c, b))
  link[b].append((c, a))

# 다이스트라
start(A)