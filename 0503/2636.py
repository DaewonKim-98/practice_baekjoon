from collections import deque

def bfs(r, c):
  visited = [[0] * M for _ in range(N)]
  q = deque()
  visited[r][c] = 1
  q.append((r, c))
  
  while q:
    r, c = q.popleft()
    
    for d in dir:
      nr, nc = r + d[0], c + d[1]
      if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0:
        # 공기면 반복
        if arr[nr][nc] == 0:
          q.append((nr, nc))
          visited[nr][nc] = 1
        # 공기랑 접촉하는 치즈면 표시
        elif arr[nr][nc] == 1:
          arr[nr][nc] = -1
          visited[nr][nc] = 1

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

# 치즈 녹이기
time = 0
lastRemainCheese = 0
while True:
  isCheese = False
  # bfs를 통해 외부 공기랑 접촉한 치즈 표시
  bfs(0, 0)
  remainCheese = 0
  # 공기랑 접촉한 치즈 제거
  for r in range(N):
    for c in range(M):
      if arr[r][c] == -1:
        isCheese = True
        arr[r][c] = 0
        remainCheese += 1
  # 만약 제거하는 치즈가 하나도 없으면 끝이므로
  if isCheese == False:
    print(time)
    print(lastRemainCheese)
    break
  lastRemainCheese = remainCheese
  time += 1
  
  