from collections import deque

dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def bfs(r, c):
  global pang
  q = deque()
  visited = [[0] * 6 for _ in range(12)]
  q.append((r, c))
  visited[r][c] = 1
  cnt = 1
  
  while q:
    r, c = q.popleft()
    # cnt가 4 이상이 되면 팡이므로
    if cnt == 4:
      pang = True
    for d in dir:
      nr, nc = r + d[0], c + d[1]
      if 0 <= nr < 12 and 0 <= nc < 6 and visited[nr][nc] == 0 and arr[nr][nc] == arr[r][c]:
        q.append((nr, nc))
        visited[nr][nc] = 1
        cnt += 1
  # 똑같은 색깔을 모두 돌았을 때 cnt가 4 이상이면 다 없애면 되므로
  if cnt >= 4:
    for r in range(12):
      for c in range(6):
        if visited[r][c] == 1:
          arr[r][c] = '.'

arr = [list(input()) for _ in range(12)]

# bfs를 통해 연결된 뿌요 찾고 제거 후 내리고 다시 찾고 반복
chain = 0
while True:
  # 터졌는지 체크
  pang = False
  for r in range(12):
    for c in range(6):
      if arr[r][c] != '.':
        bfs(r, c)
        
  # 터졌으면 연쇄 +1
  if pang == True:
    chain += 1
    # 뿌요들 모두 떨어뜨리기 - 떨어뜨릴 수 있을만큼 계속 떨어뜨리기
    while True:
      canDown = False
      for r in range(10, -1, -1):
        for c in range(6):
          if arr[r + 1][c] == '.' and arr[r][c] != '.':
            canDown = True
            arr[r + 1][c] = arr[r][c]
            arr[r][c] = '.'
      # 떨어뜨릴 수 없으면
      if canDown == False:
        break
  # 안터졌으면 그냥 끝내면 되므로
  else:
    break
  
print(chain)
