N = int(input())
arr = list(input())

# dp
dp = [1000001] * (N)
dp[0] = 0
for i in range(1, N):
  # 이전 것들을 돌면서 최소 에너지 찾기
  for j in range(i):
    if arr[i] == 'B':
      if arr[j] == 'J':
        dp[i] = min(dp[i], dp[j] + (i - j) ** 2)
    elif arr[i] == 'O':
      if arr[j] == 'B':
        dp[i] = min(dp[i], dp[j] + (i - j) ** 2)
    else:
      if arr[j] == 'O':
        dp[i] = min(dp[i], dp[j] + (i - j) ** 2)
        
# 마지막 값이 1000001이면 마지막까지 못온 것이므로
if dp[N - 1] == 1000001:
  print(-1)
else:
  print(dp[N - 1])