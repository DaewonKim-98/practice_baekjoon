N, S, M = map(int, input().split())
arr = [0] + list(map(int, input().split()))

# dp
dp = [set() for _ in range(N + 1)]
if S + arr[1] <= M:
    dp[1].add(S + arr[1])
if S - arr[1] >= 0:
    dp[1].add(S - arr[1])

for i in range(2, N + 1):
    for j in dp[i - 1]:
        if j + arr[i] <= M:
            dp[i].add(j + arr[i])
        if j - arr[i] >= 0:
            dp[i].add(j - arr[i])
if dp[N]:
    print(max(dp[N]))
else:
    print(-1)