from collections import deque
import sys
input = sys.stdin.readline

def goTop(r, c):
  q = deque()
  visited = set()
  q.append((r, c, 0))
  visited.add((r, c))

  while q:
    r, c, cnt = q.popleft()
    if r == T:
      print(cnt)
      return
    
    for i in range(r - 2, r + 3):
      for j in range(c - 2, c + 3):
        if (i, j) in holes and (i, j) not in visited:
          q.append((i, j, cnt + 1))
          visited.add((i, j))

  # 없으면
  print(-1)
  return

N, T = map(int, input().strip().split())
holes = set()
for _ in range(N):
  y, x = map(int, input().strip().split())
  holes.add((x, y))

# 0,0부터 시작해서 정상까지 ㄱㄱ
goTop(0, 0)