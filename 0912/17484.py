N, M = map(int, input().split())

arr = [[100] + list(map(int, input().split())) + [100] for _ in range(N)]

# dp를 이용해 찾기 - 양 옆에 벽을 세워주기
dp = [[1000] * (M + 2) for _ in range(N)]

# 처음에는 첫 줄만 넣기
for i in range(1, M + 1):
    dp[0][i] = arr[0][i]
# 둘쨋줄에는 들어갈 수 있는 최솟값
for i in range(1, M + 1):
    dp[1][i] = min(dp[0][i - 1], dp[0][i], dp[0][i + 1]) + arr[1][i]

# 셋째줄부터는 앞앞부터 생각해서 자신까지 오는 경로를 생각해서 최댓값 생각
for i in range(2, N):
    for j in range(1, M + 1):
        left, center, right = 1000, 1000, 1000
        dp[i][j] = min(arr[i - 1][j - 1] + dp[i - 2][j - 1], arr[i - 1][j - 1] + dp[i - 2][j], arr[i - 1][j] + dp[i - 2][j - 1], arr[i - 1][j] + dp[i - 2][j + 1], arr[i - 1][j + 1] + dp[i - 2][j], arr[i - 1][j + 1] + dp[i - 2][j + 1]) + arr[i][j]

print(min(dp[N - 1]))