N = int(input())
arr = [[0] * 101 for _ in range(101)]

dir = [[0, 1], [-1, 0], [0, -1], [1, 0]]

for i in range(N):
  c, r, d, g = map(int, input().split())
  dragon = set()
  # 끝점 x, y는
  x, y = r + dir[d][0], c + dir[d][1]
  dragon.add((r, c))
  dragon.add((x, y))

  # 커브 돌리기
  for i in range(g):
    # 모든 점이 끝점을 기준으로 시계 방향으로 90도
    nx, ny = x, y
    for nr, nc in list(dragon):
      dragon.add((nx - (ny - nc), ny - (nr - nx)))
      if nr == r and nc == c:
        x, y = x - (y - nc), y - (nr - x)
  # 모든 드래곤 좌표에 추가
  for r, c in list(dragon):
    arr[r][c] = 1

# 4개가 모두 드래곤 커브 일부 찾기
cnt = 0
for r in range(1, 101):
  for c in range(1, 101):
    isDragon = True
    for i in range(2):
      for j in range(2):
        if arr[r - i][c - j] == 0:
          isDragon = False

    if isDragon == True:
      cnt += 1

print(cnt)