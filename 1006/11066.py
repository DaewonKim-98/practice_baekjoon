T = int(input())

for case in range(1, T + 1):
    K = int(input())
    arr = list(map(int, input().split()))

    # 인접한 것들을 계속 더하면서 최솟값 찾기
    # 2차원 배열
    dp = [[0] * K for _ in range(K)]
    # 처음 dp는 각 수들의 합
    for i in range(K - 1):
        dp[1][i] = arr[i] + arr[i + 1]

    # K = 3일 때까지 dp는 이전 dp와 arr에 따라서
    for i in range(0, K - 2):
        dp[2][i] = min(dp[1][i] + arr[i + 2] + dp[1][i], dp[1][i + 1] + arr[i] + dp[1][i + 1])


    # 이후에는 자신 아래아래의 dp까지 고려해서
    for i in range(3, K):
        for j in range(0, K - i):
            dp[i][j] = min(dp[i - 1][j] + arr[j + 3] + dp[i - 1][j], 
                               dp[i - 1][j + 1] + arr[j] + dp[i - 1][j + 1], 
                               dp[i - 2][j] * 2 + dp[i - 2][j + 2] * 2)

    print(dp)