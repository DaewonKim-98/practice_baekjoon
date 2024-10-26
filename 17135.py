from collections import deque
from itertools import combinations
from copy import deepcopy

dir = [[0, -1], [-1, 0], [0, 1]]

def deleteEnemy(archer):
  q = deque()
  q.append((N - 1, archer))
  visited = [[0] * M for _ in range(N)]
  visited[N - 1][archer] = 1

  while q:
    r, c = q.popleft()
    # 적이 있으면
    if arrCopy[r][c] > 0:
      arrCopy[r][c] += 1
      return
    
    for d in dir:
      nr, nc = r + d[0], c + d[1]
      if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and abs(N - nr) + abs(archer - nc) <= D:
        visited[nr][nc] = 1
        q.append((nr, nc))


N, M, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 궁수가 있을 수 있는 경우의 수
castle = [i for i in range(M)]
archersCases = combinations(castle, 3)

maxCnt = 0
for archerCase in archersCases:
  cnt = 0
  arrCopy = deepcopy(arr)
  # N턴이 지나면 적들은 모두 사라지므로
  for _ in range(N):
    # 궁수의 위치에서 가장 가까운 적 섬멸
    for archer in archerCase:
      # 가장 가까운 적 제거
      deleteEnemy(archer)
      
    # 섬멸받은 적들 제거
    for r in range(N):
      for c in range(M):
        if arrCopy[r][c] > 1:
          cnt += 1
          arrCopy[r][c] = 0
    # 적들 아래로
    for r in range(N - 2, -1, -1):
      for c in range(M):
        arrCopy[r + 1][c] = arrCopy[r][c]
    for c in range(M):
      arrCopy[0][c] = 0

  maxCnt = max(maxCnt, cnt)

print(maxCnt)