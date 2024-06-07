import heapq

def bfs(a):
  global length
  robot1 = []
  heapq.heappush(robot1, (0, 0, a))
  
  while robot1:
    # 현재까지의 거리, 거리 중에서의 최대, 현재 통로
    aLength, maxLength, a = heapq.heappop(robot1)
    
    # 방문하지 않았으면
    if visited[a] == 0:
      visited[a] = 1
      for i in link[a]:
        # b를 만나면 끝이므로
        if i[0] == b:
          length = aLength + i[1] - max(maxLength, i[1])
          # print(aLength + i[1] - max(maxLength, i[1]))
          return
        
        # 계속 연결
        heapq.heappush(robot1, (aLength + i[1], max(maxLength, i[1]), i[0]))
          
      

N, a, b = map(int, input().split())
link = [set() for _ in range(N + 1)]
# 통로 연결
for _ in range(N - 1):
  s, e, l = map(int, input().split())
  link[s].add((e, l))
  link[s].add((s, 0))
  link[e].add((s, l))
  link[e].add((e, 0))
  
# bfs를 통해
visited = [0] * (N + 1)
length = 0
bfs(a)
print(length)