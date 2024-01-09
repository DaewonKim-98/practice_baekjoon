T = int(input())
for case in range(1, T + 1):
    arr = list(map(int, input().split()))
    N = arr.pop(0)
    S = 0
    # 정렬후 누적합
    arr.sort()
    arr = [0] + arr
    for i in range(1, N + 1):
        arr[i] += arr[i - 1]
    for M in range(1, N + 1):
        # dp
        dp = [4000000] * (N + 1)
        # 각각 dp는 최댓값 * M - 합이므로
        for i in range(M, N + 1):
            dp[i] = min(dp[i - 1], (arr[i] - arr[i - 1]) * M - (arr[i] - arr[i - M]))
        # print(dp)
        S += dp[N]
    print(S)