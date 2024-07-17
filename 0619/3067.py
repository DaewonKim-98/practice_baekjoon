import sys
input = sys.stdin.readline

def makeCoin(coins, M):
    dp = [0] * (M + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(1, M + 1):
            if coin <= i:
                dp[i] += dp[i - coin]
    return dp[M]

T = int(input().strip())

for _ in range(T):
    N = int(input().strip())
    coins = list(map(int, input().strip().split()))
    M = int(input().strip())
    print(makeCoin(coins, M))