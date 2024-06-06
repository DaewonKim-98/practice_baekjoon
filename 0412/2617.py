from collections import deque

def bfs(num):
  global cnt
  q = deque()
  visited = [0] * (N + 1)
  q.append(num)
  visited[num] = 1
  cntLight = 0
  cntHeavy = 0
  
  while q:
    number = q.popleft()
    if cntLight - N//2 > 0:
      cnt += 1
      return
    for j in linkLight[number]:
      if visited[j] == 0:
        q.append(j)
        cntLight += 1
        visited[j] = 1
        
  visited = [0] * (N + 1)
  q.append(num)
  visited[num] = 1
  while q:
    number = q.popleft()
    if cntHeavy - N//2 > 0:
      cnt += 1
      return
    for j in linkHeavy[number]:
      if visited[j] == 0:
        q.append(j)
        cntHeavy += 1
        visited[j] = 1
    
  

N, M = map(int, input().split())
# 자신보다 가벼운 것들 추가
linkLight = [[] for _ in range(N + 1)]
# 자신보다 무거운 것들
linkHeavy = [[] for _ in range(N + 1)]

for _ in range(M):
  a, b = map(int, input().split())
  linkLight[a].append(b)
  linkHeavy[b].append(a)
  
# 어떤 i에 대해 자기보다 가볍거나 무거운 것들이 N//2 보다 많으면 
# 중간이 될 수 없음
cnt = 0
for i in range(1, N + 1):
  bfs(i)
  
print(cnt)