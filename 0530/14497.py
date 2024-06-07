from copy import deepcopy
from collections import deque

def padong(r, c):
  global cnt
  visited = [[0] * M for _ in range(N)]
  q = deque([])
  visited[r][c] == 1
  q.append((r, c))
  
  while q:
    r, c = q.popleft()
    # 범인에 도착하면 끝
    if r == x2 and c == y2:
      print(cnt)
      exit()
    
    for d in dir:
      nr, nc = r + d[0], c + d[1]
      if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0:
        # 학생이면 무너뜨리기
        if arr[nr][nc] == '1':
          arr[nr][nc] = '0'
          visited[nr][nc] = 1
        # 빈 공간이면 계속
        else:
          q.append((nr, nc))
          visited[nr][nc] = 1

N, M = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
x1 -= 1
y1 -= 1
x2 -= 1
y2 -= 1
arr = [list(input()) for _ in range(N)]
dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
cnt = 0

# 주난이부터 파동
while True:
  cnt += 1
  padong(x1, y1)