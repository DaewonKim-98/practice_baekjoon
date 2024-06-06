N = int(input())
arr = [0] + list(map(int, input().split()))

# bfs 시간초과 dp
# dp[i][j]는 i번째까지 j를 만들 수 있는 경우의 수
dp = [[0] * 21 for _ in range(N + 1)]
dp[1][arr[1]] = 1

for i in range(2, N):
  for j in range(21):
    # i - 1번째까지 만들어진 어떤 j에 대해 arr[i]를 더한게 범위 안이면
    # 이전 것들의 개수를 더할 수 있으므로
    if 0 <= j + arr[i] <= 20:
      dp[i][j + arr[i]] += dp[i - 1][j]
    if 0 <= j - arr[i] <= 20:
      dp[i][j - arr[i]] += dp[i - 1][j]

print(dp[N - 1][arr[-1]])