N, M, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

maxh = 0
minh = 256
for l in arr:
  maxh = max(maxh, max(l))
  minh = min(minh, min(l))

minTime = 2 * 256 * 500 * 500
maxHeight = 0
# 가장 작은 것부터 큰 것까지 땅 고르기 작업
for h in range(minh, maxh + 1):
  b = B
  time = 0
  # 땅 고르기
  for r in range(N):
    for c in range(M):
      # 땅이 낮으면 채워넣기
      if arr[r][c] < h:
        b -= (h - arr[r][c])
        time += (h - arr[r][c])
      # 땅이 높으면 파기
      else:
        b += (arr[r][c] - h)
        time += 2 * (arr[r][c] - h)
  # 다 진행했을 때 인벤토리가 남아있으면 가능한 것이므로
  if b >= 0:
    if minTime >= time:
      minTime = time
      maxHeight = max(maxHeight, h)

print(minTime, maxHeight)