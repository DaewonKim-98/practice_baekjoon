import heapq

linkDic = {}

def bfs(i):
  q = []
  heapq.heapify(q)
  heapq.heappush(q, (1, i, (1, 1)))
  
  while q:
    time, i, l = heapq.heappop(q)
    if visited[i] == 0:
      visited[i] = 1
      if i != 1:
        linkDic[i] = l
      for j in link[i]:
        heapq.heappush(q, (time + j[1], j[0], (i, j[0])))
        
  # 다 끝나면 모두 연결한 것이므로
  print(len(linkDic))
  for i in linkDic.values():
    print(i[0], i[1])

N, M = map(int, input().split())
link = [[] for _ in range(N + 1)]
for _ in range(M):
  a, b, c = map(int, input().split())
  link[a].append((b, c))
  link[b].append((a, c))
  
# 원래 네트워크에서 통신하는 최소 시간
visited = [0] * (N + 1)
bfs(1)
