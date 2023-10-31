N = int(input())

dp = [0] * (N + 1)
if N == 1:
    print(0)
elif N == 2:
    print(1)

# 24 - 2 * 4 - 1 * 6 - 1
# 120 - 9 * 5 - 2 * 10 - 10 - 1


# dp는 N! 에서 그 아래에 있는 i들에 대해 dp[i] * nCi들을 뺀 것과 같으므로
else:
    dp[1] = 0
    dp[2] = 1
    for i in range(3, N + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) * (i - 1)
        dp[i] %= 1000000000

    print(dp[N])