N, M = map(int, input().split())
arr = list(map(int, input().split()))

# 누적합
arr = [0] + arr
for i in range(1, N + 1):
  arr[i] += arr[i - 1]

maxValume = 0
i, j = 0, 0
while j <= N:
  # M보다 작으면 더 늘릴 수 있으므로
  if arr[j] - arr[i] <= M:
    maxValume = max(maxValume, arr[j] - arr[i])
    j += 1
  else:
    i += 1

print(maxValume)