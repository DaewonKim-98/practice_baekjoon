from itertools import combinations
from collections import deque

dir = [[0, 1], [1, 0], [-1, 0], [0, -1]]

def calcultateDistance(case):
  global minDistance
  q = deque()
  visited = [[0] * N for _ in range(N)]
  for r, c in case:
    q.append((r, c, r, c))
    visited[r][c] = 1
  cnt = 0
  distance = 0
  
  while q:
    cr, cc, rr, rc = q.popleft()
    # 집에 도착하면
    if arr[rr][rc] == 1:
      cnt += 1
      distance += abs(rr - cr) + abs(rc - cc)
    # 모든 집에 다 도착하기 전에 거리가 이미 최소 거리보다 커진다면
    if distance >= minDistance:
      return
    # 모든 집에 다 도착하면
    if cnt == homeCnt:
      minDistance = min(minDistance, distance)
      return
    
    for d in dir:
      nr, nc = rr + d[0], rc + d[1]
      if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
        visited[nr][nc] = 1
        q.append((cr, cc, nr, nc))

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 치킨집
stores = set()
homeCnt = 0
for r in range(N):
  for c in range(N):
    if arr[r][c] == 2:
      stores.add((r, c))
    if arr[r][c] == 1:
      homeCnt += 1

# 살아남는 치킨집의 경우의 수
storesCases = combinations(stores, M)

# 이 치킨집들만 살아남았을 때 치킨 거리 최솟값
minDistance = 100 * 13
for storeCase in storesCases:
  calcultateDistance(storeCase)

print(minDistance)