N, M = map(int, input().split())
arr = [[0] * (M + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

# 누적합
for r in range(1, N + 1):
  for c in range(1, M + 1):
    arr[r][c] += arr[r][c - 1] + arr[r - 1][c] - arr[r - 1][c - 1]

# 최댓값
maxValue = -10000 * 200 * 200
for r in range(1, N + 1):
  for c in range(1, M + 1):
    for i in range(r):
      for j in range(c):
        maxValue = max(maxValue, arr[r][c] - arr[i][c] - arr[r][j] + arr[i][j])

print(maxValue)