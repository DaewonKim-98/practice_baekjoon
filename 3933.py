# dp인듯?
# dp[i][j]는 i를 j개의 제곱수로 나타내는 경우의 수
dp = [[0] * 5 for _ in range(2 ** 15 + 1)]
dp[0][0] = 1
for i in range(1, 2 ** 14 + 1):
    for j in range(1, 5):
        for k in range(i ** 2, 2 ** 15 + 1):
            dp[k][j] += dp[k - (i ** 2)][j - 1]
            
while True:
    N = int(input())
    if N == 0:
        break
    print(sum(dp[N]))