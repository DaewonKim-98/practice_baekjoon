N = int(input())

dp = [0] * (N + 1)
if N == 1:
  print(1)
  exit()

dp[1] = 1
for i in range(1, N + 1):
  