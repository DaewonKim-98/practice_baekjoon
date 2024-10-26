N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
# dp[i][j]는 i행 j까지의 최댓값
dp[0][0] = arr[0][0]
for i in range(1, N):
  for j in range(i + 1):
    dp[i][j] = arr[i][j] + max(dp[i - 1][j], dp[i - 1][j - 1])
# print(dp)
print(max(dp[N - 1]))