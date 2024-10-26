direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]

N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

cnt = 0

while True:
  # 현재 칸이 청소되지 않은 경우
  if arr[r][c] == 0:
    # 청소
    arr[r][c] = -1
    cnt += 1

  # 주변 4칸 중 청소되지 않은 빈 칸 있는지 찾기
  canClean = False
  for dir in direction:
    nr, nc = r + dir[0], c + dir[1]
    if arr[nr][nc] == 0:
      canClean = True
      break
  
  # 빈 칸이 없으면
  if canClean == False:
    # 현재 바라보는 방향을 유지한 채로 후진
    # 후진할 수 없다면 작동 멈추기
    if arr[r - direction[d][0]][c - direction[d][1]] == 1:
      break
    # 후진할 수 있으면 후진
    else:
      r -= direction[d][0]
      c -= direction[d][1]
  
  # 청소되지 않은 빈 칸이 있으면
  else:
    while True:
      # 반시계 방향으로 회전
      d += 4
      d -= 1
      d %= 4
      # 앞 칸이 청소되지 않은 빈 칸이면 전진
      if arr[r + direction[d][0]][c + direction[d][1]] == 0:
        r += direction[d][0]
        c += direction[d][1]
        break

print(cnt)