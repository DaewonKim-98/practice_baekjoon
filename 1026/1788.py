N = int(input())

# 또 dppdpdpdpdpdpdpdpdpddpdpdpdpdpdppdpdpdppdpdpdppddppdpdpdpddpdpdpdpdpdpdpdpdpdpdpdppd
dp = [0] * 2000001
dp[1000000] = 0
dp[1000001] = 1

# 가운데부터 dp 시작
for i in range(1000002, 2000001):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000000

# 음수 부분도 dp로 채우기
for i in range(999999, -1, -1):
    if dp[i + 2] - dp[i + 1] >= 0:
        dp[i] = (dp[i + 2] - dp[i + 1]) % 1000000000
    else:
        dp[i] = - (abs(dp[i + 2] - dp[i + 1]) % 1000000000)

N = N + 1000000
if dp[N] > 0:
    print(1)
    print(dp[N])
elif dp[N] == 0:
    print(0)
    print(0)
else:
    print(-1)
    print(-dp[N])