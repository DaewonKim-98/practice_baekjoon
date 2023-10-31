N = int(input())
arr = list(map(int, input().split()))

# dp로?
dp = [0] * N

# 2번째까지는 그 사이의 차가 최대이므로
if N == 1:
    print(1)
elif N == 2:
    print(max(arr) - min(arr))
# 3번째부터 시작
else:
    dp[0] = 0
    dp[1] = max(arr[0:2]) - min(arr[0:2])
    for i in range(2, N):
        for j in range(0, i):
            dp[i] = max(dp[j] + max(arr[j + 1:i + 1]) - min(arr[j + 1:i + 1]), dp[i])

print(dp[N - 1])