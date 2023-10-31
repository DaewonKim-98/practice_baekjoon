N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]
dp[0][0] = 0
dp[arr[0][0]][0] = 1
dp[0][arr[0][0]] = 1
# print(dp)

for r in range(N):
    for c in range(N):
        if r == N - 1 and c == N - 1:
            print(dp[N - 1][N - 1])
            exit()
        if dp[r][c] != 0:
            if r + arr[r][c] < N:
                dp[r + arr[r][c]][c] = dp[r + arr[r][c]][c] + dp[r][c]
            if c + arr[r][c] < N:
                dp[r][c + arr[r][c]] = dp[r][c + arr[r][c]] + dp[r][c]

        # print(dp)