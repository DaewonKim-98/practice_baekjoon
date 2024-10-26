from collections import deque

dir = [[-1, 0], [0, -1], [1, 0], [0, 1]]

def findPassenger(r, c):
  q = deque()
  q.append((r, c))
  visited = [[0] * N for _ in range(N)]
  visited[r][c] = 1

  while q:
    r, c = q.popleft()
    if (r, c) in move.keys():
      while q:
        nr, nc = q.popleft()
        if visited[nr][nc] > visited[r][c]:
          break
        if (nr, nc) in move.keys():
          if r > nr:
            r, c = nr, nc
          elif r == nr and c > nc:
            r, c = nr, nc
      return [r, c, visited[r][c] - 1]
    
    for d in dir:
      nr, nc = r + d[0], c + d[1]
      if 0 <= nr < N and 0 <= nc < N and arr[r][c] != 1 and visited[nr][nc] == 0:
        visited[nr][nc] = visited[r][c] + 1
        q.append((nr, nc))
  
  print(-1)
  exit()

def goDestination(pr, pc):
  q = deque()
  q.append((pr, pc))
  visited = [[0] * N for _ in range(N)]
  visited[pr][pc] = 1

  while q:
    r, c = q.popleft()
    # 도착지에 도착하면
    if (r, c) == move[(pr, pc)]:
      return [r, c, visited[r][c] - 1]
    
    for d in dir:
      nr, nc = r + d[0], c + d[1]
      if 0 <= nr < N and 0 <= nc < N and arr[r][c] != 1 and visited[nr][nc] == 0:
        visited[nr][nc] = visited[r][c] + 1
        q.append((nr, nc))  

  print(-1)
  exit()

N, M, F = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dr, dc = list(map(int, input().split()))
dr -= 1
dc -= 1
move = {}
for i in range(1, M + 1):
  a, b, c, d = map(int, input().split())
  move[(a - 1, b - 1)] = (c - 1, d - 1)

for _ in range(M):
  # 현재 위치에서 출발지까지 이동
  pr, pc, f = findPassenger(dr, dc)
  # 고객의 출발지까지 이동할 때 연료가 모두 소모되면 끝이므로
  if F <= f:
    print(-1)
    exit()
  F -= f
  # 고객의 도착지까지 이동
  dr, dc, f = goDestination(pr, pc)
  # 이동했을 때 연료가 모두 소모되면 끝이므로
  if F < f:
    print(-1)
    exit()
  F -= f
  F += f * 2
  del move[(pr, pc)]

# 남은 연료의 양
print(F)