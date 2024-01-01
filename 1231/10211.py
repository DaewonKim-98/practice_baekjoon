T = int(input())

for case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    dp = [-1000] * (N + 1)
    for i in range(1, N + 1):
        dp[i] = max(arr[i - 1], dp[i - 1] + arr[i - 1])
        
    print(max(dp))