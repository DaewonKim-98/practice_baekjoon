T = int(input())
for _ in range(T):
    n = int(input())
    arr0 = list(map(int, input().split()))
    arr1 = list(map(int, input().split()))

    # dp[i, j]는 i번째의 j일 때 스티커의 합의 최대
    dp = [[0] * 2 for _ in range(n)]
    dp[0][0] = arr0[0]
    dp[0][1] = arr1[0]
    
    # dp[i]는 i - 1의 j가 아닐 때 + arrj[i]와 i - 1의 그냥 j일때 중 최댓값
    for i in range(1, n):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + arr0[i])
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + arr1[i])
        
    print(max(dp[n - 1]))