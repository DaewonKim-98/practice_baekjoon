from collections import deque

def bfs(i):
  q = deque()
  q.append(i)

  while q:
    i = q.popleft()
    # 친구의 친구 이상은 친구가 아니므로
    if visited[i] == 3:
      return
    for j in link[i]:
      if visited[j] == 0:
        visited[j] = visited[i] + 1
        q.append(j)

N = int(input())
M = int(input())
link = [set() for _ in range(N + 1)]

for _ in range(M):
  a, b = map(int, input().split())
  link[a].add(b)
  link[b].add(a)
  
# bfs를 통해 친구 수 출력
visited = [0] * (N + 1)
visited[1] = 1
bfs(1)

cnt = 0
for v in visited:
  if v > 1:
    cnt += 1
print(cnt)