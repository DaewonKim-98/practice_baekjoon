dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def bfs(r, c, animal):
  global last_sheep
  global last_wolf
  q = []
  q.append((r, c))
  visited[r][c] = 1
  sheep = 0
  wolf = 0
  if animal == 'o':
    sheep += 1
  elif animal == 'v':
    wolf += 1
    
  while q:
    r, c = q.pop(0)
    # print(r, c)
    
    for d in dir:
      nr, nc = r + d[0], c + d[1]
      if 0 <= nr < R and 0 <= nc < C and visited[nr][nc] == 0 and arr[nr][nc] != '#':
        q.append((nr, nc))
        visited[nr][nc] = 1
        if arr[nr][nc] == 'o':
          sheep += 1
        elif arr[nr][nc] == 'v':
          wolf += 1
          
  # 다 돌고 양이 늑대보다 많으면 늑대 die
  # print(sheep)
  # print(wolf)
  if sheep > wolf:
    last_sheep += sheep
  else:
    last_wolf += wolf
        
        
R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]

# bfs를 통해 양과 늑대 찾고 계산
visited = [[0] * C for _ in range(R)]

last_sheep = 0
last_wolf = 0
for r in range(R):
  for c in range(C):
    if visited[r][c] == 0 and arr[r][c] != '#':
      bfs(r, c, arr[r][c])
      
print(last_sheep, last_wolf)