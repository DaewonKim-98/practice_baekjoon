from itertools import combinations
from copy import deepcopy
from collections import deque

dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def bfs(r, c):
  q = deque()
  visited[r][c] = 1
  q.append((r, c))
  
  while q:
    r, c = q.popleft()
    for d in dir:
      nr, nc = r + d[0], c + d[1]
      if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and arr_copy[nr][nc] == 0:
        q.append((nr, nc))
        arr_copy[nr][nc] = 2
        visited[nr][nc] = 1

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 벽 세우는 것 전체에서 조합으로
blank = []
for r in range(N):
  for c in range(M):
    if arr[r][c] == 0:
      blank.append([r, c])
      
wall_combination = list(combinations(blank, 3))
# 벽 세우고 bfs로 바이러스 퍼뜨리고 안전 영역 최대 크기 찾기
max_safe_zone = 0
for wall in wall_combination:
  # 벽 세우기
  arr_copy = deepcopy(arr)
  for i in wall:
    arr_copy[i[0]][i[1]] = 1
    
  # 바이러스 퍼뜨리기
  visited = [[0] * M for _ in range(N)]
  for r in range(N):
    for c in range(M):
      if arr_copy[r][c] == 2 and visited[r][c] == 0:
        bfs(r, c)
  
  # 안전 영역 찾기
  safe_zone = 0
  for r in range(N):
    for c in range(M):
      if arr_copy[r][c] == 0:
        safe_zone += 1
  
  # 갱신
  max_safe_zone = max(max_safe_zone, safe_zone)
  
print(max_safe_zone)