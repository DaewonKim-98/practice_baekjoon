a = list(input())
b = list(input())
c = list(input())

x, y, z = len(a), len(b), len(c)

# dp[i][j][k]는 i, j, k 번째의 최대 공통된 수열
dp = [[[0] * (z + 1) for _ in range(y + 1)] for _ in range(x + 1)]

for i in range(1, x + 1):
  for j in range(1, y + 1):
    for k in range(1, z + 1):
      # 셋 다 똑같으면 공통된 것이므로
      if a[i - 1] == b[j - 1] == c[k - 1]:
        dp[i][j][k] += dp[i  -1][j - 1][k - 1] + 1
        
      # 다르면 이전의 최댓값으로
      else:
        dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])

print(dp[x][y][z])