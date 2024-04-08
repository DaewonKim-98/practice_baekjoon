import heapq

def bfs(s):
  visited = [0] * (N + 1)
  q = []
  heapq.heappush(q, (0, s))
  
  while q:
    weight, i = heapq.heappop(q)
    if visited[i] == 0:
      visited[i] = 1
      # t를 만나면
      if i == t:
        print(weight)
        return
      
      for j in link[i]:
        if visited[j[0]] == 0:
          heapq.heappush(q, (weight + j[1], j[0]))
      

N, M = map(int, input().split())
link = [[] for _ in range(N + 1)]
for _ in range(M):
  a, b, c = map(int, input().split())
  link[a].append((b, c))
  link[b].append((a, c))
  
s, t = map(int, input().split())
# s에서 시작해서 t로 다이스트라
bfs(s)