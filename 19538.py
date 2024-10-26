import sys
from collections import deque
input = sys.stdin.readline

def spreadRumor():
  q = deque()
  for i in rumorer:
    q.append(i)

  newRumorer = deque()
  while q:
    i = q.popleft()

    # 다음 유포자 찾기
    for j in link[i]:
      if visited[j] == -1:
        cnt = 0
        for k in link[j]:
          if visited[k] != -1:
            cnt += 1
        if cnt >= (len(link[j]) + 1) // 2:
          newRumorer.append(j)
    if not q:
      while newRumorer:
        r = newRumorer.popleft()
        visited[r] = visited[i] + 1
        q.append(r)

N = int(input().strip())
link = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
  arr = list(map(int, input().strip().split()))
  for l in arr:
    if l == 0:
      break
    link[i].append(l)
    link[l].append(i)

M = int(input().strip())
rumorer = set(map(int, input().strip().split()))

visited = [-1] * (N + 1)
for i in rumorer:
  visited[i] = 0

# bfs로
spreadRumor()
for i in range(1, N + 1):
  print(visited[i], end=' ')