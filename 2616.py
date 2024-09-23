N = int(input())
arr = list(map(int, input().split()))
M = int(input())

# 누적합
for i in range(1, N):
  arr[i] = arr[i] + arr[i - 1]
arr = [0] + arr
# dp[i][1]는 i번째까지 j개로 끌 수 있는 최대 손님 수
dp = [[0] * 4 for _ in range(N + 1)]
dp[M - 1][1] = arr[M - 1]

for i in range(1, 4):
  for j in range(i * M, N + 1):
    dp[j][i] = max(dp[j - 1][i], dp[j - M][i - 1] + arr[j] - arr[j - M])
print(dp[N][3])