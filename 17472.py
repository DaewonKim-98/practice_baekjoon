from collections import deque
import heapq

dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def numbering(r, c, number):
  q = deque()
  q.append((r, c))

  while q:
    r, c = q.popleft()
    arr[r][c] = number

    for d in dir:
      nr, nc = r + d[0], c + d[1]
      if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 1:
        q.append((nr, nc))

def linking(r, c, num):
  # 자기 섬에서부터 출발해서 다른 섬 찾기
  q = deque()
  ivisited = [[0] * M for _ in range(N)]
  q.append((r, c, num))
  ivisited[r][c] = 1

  while q:
    r, c, num = q.popleft()

    for d in dir:
      nr, nc = r + d[0], c + d[1]
      if 0 <= nr < N and 0 <= nc < M and ivisited[nr][nc] == 0:
        # 섬이면
        if arr[nr][nc] == num:
          ivisited[nr][nc] = 1
          q.append((nr, nc, num))
        # 바다면 다리를 놓고 그 섬에서 다시 탐색
        else:
          l = 0
          while 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:
            nr += d[0]
            nc += d[1]
            l += 1
          # 방문하지 않은 섬에 도착했으면
          if 0 <= nr < N and 0 <= nc < M and l >= 2 and (arr[nr][nc], l) not in link[num]:
            link[num].add((arr[nr][nc], l))
            link[arr[nr][nc]].add((num, l))
            ivisited[nr][nc] = 1
            q.append((nr, nc, arr[nr][nc]))

def findMinLength():
  q = []
  heapq.heappush(q, (0, 2))
  visited = [0] * (i + 1)
  cnt = 0

  while q:
    length, bridge = heapq.heappop(q)
    if visited[bridge] == 0:
      visited[bridge] = 1
      cnt += length
      
      for j in link[bridge]:
        heapq.heappush(q, (j[1], j[0]))

  # 모두 연결되었으면 최소로 연결되었다는 것이므로
  print(cnt)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 다른 섬들 구분
i = 1
ir, ic = 0, 0
for r in range(N):
  for c in range(M):
    if arr[r][c] == 1:
      i += 1
      numbering(r, c, i)
      ir, ic = r, c

# 다른 섬으로 연결
canLink = False
link = [set() for _ in range(i + 1)]
cnt = 0
linking(ir, ic, i)
# 연결된 섬의 개수
for l in link:
  if l:
    cnt += 1
if cnt != i - 1:
  print(-1)
else:
  # 다리 길이의 최솟값
  findMinLength()