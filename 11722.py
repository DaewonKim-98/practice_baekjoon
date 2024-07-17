N = int(input())
arr = list(map(int, input().split()))

# dp[i]는 i까지 가장 긴 감소하는 부분 수열
dp = [1] * N
for i in range(1, N):
    for j in range(i + 1):
        if arr[j] > arr[i]:
            dp[i] = max(dp[j] + 1, dp[i])
            
print(max(dp))