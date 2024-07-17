N = int(input())
arr = list(map(int, input().split()))

# 제거하지 않았을 때
# dp[i - 1]는 i번째까지 큰 합
dp = [0] * N
dp[0] = arr[0]

for i in range(1, N):
    dp[i] = max(dp[i - 1] + arr[i], arr[i])
    
# 제거했을 때
# ndp[i - 1]는 i번째까지 큰 합
ndp = [0] * N
ndp[0] = arr[0]

for i in range(1, N):
    ndp[i] = max(dp[i - 1] - arr[i - 1] + arr[i], arr[i], ndp[i - 1] + arr[i])
    
print(max(max(ndp), max(dp)))