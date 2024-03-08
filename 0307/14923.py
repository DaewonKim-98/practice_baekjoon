from collections import deque
from copy import deepcopy

dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def bfs(r, c, arr):
  global time
  q = deque()
  visited[r][c][0] = 1
  visited[r][c][1] = 1
  q.append((r, c, False))
  
  while q:
    r, c, isBreak = q.popleft()
    # 탈출구에 도착하면
    if r == ex and c == ey:
      if visited[r][c][0] != 0:
        time = visited[r][c][0] - 1
      else:
        time = visited[r][c][1] - 1
      return
    
    for d in dir:
      nr, nc = r + d[0], c + d[1]
      if 0 <= nr < N and 0 <= nc < M:
        # 벽을 부순 상태이면 무조건 0으로만
        if isBreak == True:
          if visited[nr][nc][0] == 0 and arr[nr][nc] == 0:
            visited[nr][nc][0] = visited[r][c][0] + 1
            q.append((nr, nc, True))
        # 벽을 부수지 않은 상태이면 1로 가도 되므로
        if isBreak == False:
          # 1로 갔을 때에는 벽을 부수고 간 것이므로 벽 부쉈다는 처리
          if visited[nr][nc][0] == 0 and arr[nr][nc] == 1:
            visited[nr][nc][0] = visited[r][c][0] + 1
            q.append((nr, nc, True))
          # 벽을 안부수고 가는거는 쭉 계속 가도 되므로
          elif visited[nr][nc][1] == 0 and arr[nr][nc] == 0:
            visited[nr][nc][0] = visited[r][c][0] + 1
            visited[nr][nc][1] = visited[r][c][1] + 1
            q.append((nr, nc, False))

N, M = map(int, input().split())
hx, hy = map(int, input().split())
ex, ey = map(int, input().split())
hx -= 1
hy -=1
ex -= 1
ey -= 1
arr = [list(map(int, input().split())) for _ in range(N)]

# 일단 bfs를 통해 찾고
time = -1
# 벽을 부수고 갈 때, 벽을 안부수고 갈 때의 visited
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
# print(visited)
bfs(hx, hy, arr)
# print(visited)
# # 벽을 없애고 bfs를 통해 찾기
# for r in range(N):
#   for c in range(M):
#     arrCopy = deepcopy(arr)
#     if arrCopy[r][c] == 1:
#       arrCopy[r][c] = 0
#       bfs(hx, hy, arrCopy)
      
print(time)