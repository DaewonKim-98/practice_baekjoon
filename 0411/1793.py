import sys
input = sys.stdin.readline

dp = [0] * 251
dp[0] = 0
dp[1] = 1
dp[2] = 3

for i in range(3, 251):
  dp[i] = dp[i - 1] + dp[i - 2] * 2


while True:
  try:
    N = int(input().strip())
    if N == 0:
      print(1)
    else:
      print(dp[N])
  except:
    break