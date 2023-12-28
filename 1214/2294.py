N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

# 디디디디디디디피피피피피빠삐코 또 너냐!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# K를 만드는 최소 경우를 dp
dp = [0] * (K + 1)

for i in range(K + 1):
    dp[i] = 10001
    for coin in arr:
        if i // coin == 1 and i % coin == 0:
            dp[i] = 1
        elif i // coin > 0:
            dp[i] = min(dp[i - coin] + 1, dp[i])

# print(dp)      
if dp[K] == 10001:
    # 이면 만들 수 없다는 것이므로
    print(-1)
else:
    print(dp[K])