import sys
input = sys.stdin.readline

# dp[i][j]는 정수 i를 마지막 j를 더해서 만든 경우의 수
dp = [[0] * 4 for _ in range(100000 + 1)]
dp[1][1] = 1
dp[2][2] = 1
dp[3][1] = 1
dp[3][2] = 1
dp[3][3] = 1
  
for i in range(4, 100000 + 1):
  dp[i][1] = (dp[i - 1][2] + dp[i - 1][3]) % 1000000009
  dp[i][2] = (dp[i - 2][1] + dp[i - 2][3]) % 1000000009
  dp[i][3] = (dp[i - 3][1] + dp[i - 3][2]) % 1000000009
T = int(input().strip())
for case in range(1, T + 1):
  N = int(input().strip())
  
  print(sum(dp[N]) % 1000000009)
