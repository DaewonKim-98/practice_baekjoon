N = int(input())
arr = list(map(int, input().split()))

dp = [0] * (N + 1)
dp[1] = arr[0]
for i in range(2, N + 1):
    # 처음 dp는 자기 자신의 카드
    dp[i] = arr[i - 1]
    # 최솟값을 찾아야 하는데 자신보다 1 작은거 + arr[0], 2 작은거 + arr[1], ...
    for j in range(1, i):
        dp[i] = min(dp[i], dp[i - j] + arr[j - 1])
# print(dp)
print(dp[N])