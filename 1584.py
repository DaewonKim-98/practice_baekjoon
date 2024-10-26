import heapq

dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def findRoad(r, c):
  q = []
  heapq.heapify(q)
  heapq.heappush(q, (0, r, c))
  visited = [[0] * 501 for _ in range(501)]
  visited[r][c] = 1

  while q:
    l, r, c = heapq.heappop(q)
    if r == 500 and c == 500:
      print(l)
      return
    for d in dir:
      nr, nc = r + d[0], c + d[1]
      # 안전한 구역이면 그냥 ㄱㄱ
      if 0 <= nr < 501 and 0 <= nc < 501 and arr[nr][nc] == 0 and visited[nr][nc] == 0:
        heapq.heappush(q, (l, nr, nc))
        visited[nr][nc] = 1
      # 오염된 곳이면 1 추가
      elif 0 <= nr < 501 and 0 <= nc < 501 and arr[nr][nc] == 1 and visited[nr][nc] == 0:
        heapq.heappush(q, (l + 1, nr, nc))
        visited[nr][nc] = 1
  # print(visited)
  # 도착을 못하면
  print(-1)
  return

arr = [[0] * 501 for _ in range(501)]
N = int(input())
for _ in range(N):
  x, y, z, w = map(int, input().split())
  for r in range(min(x, z), max(x, z) + 1):
    for c in range(min(y, w), max(y, w) + 1):
      arr[r][c] = 1
M = int(input())
for _ in range(M):
  x, y, z, w = map(int, input().split())
  for r in range(min(x, z), max(x, z) + 1):
    for c in range(min(y, w), max(y, w) + 1):
      arr[r][c] = -1
# print(arr)
# bfs를 통해 길 찾기
findRoad(0, 0)