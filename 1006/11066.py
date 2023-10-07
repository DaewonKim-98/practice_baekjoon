T = int(input())

for case in range(1, T + 1):
    K = int(input())
    arr = list(map(int, input().split()))

    # 인접한 것들을 계속 더하면서 최솟값 찾기
    # 2차원 배열
    dp = [[0] * (K + 1) for _ in range(K + 1)]
    # 처음 dp는 각 수들의 합
    for i in range(1, K):
        dp[i][i + 1] = arr[i - 1] + arr[i]


    # 1, 4는 1, 1 + 2, 4 / 1, 2 + 3, 4 / 1, 3 + 4, 4로 이루어져있으므로
    # 이후도 똑같을 것?????일걸??맞나제발
    # 밑에서부터 i가 올라와야지 1부터의 합을 구할 수 있으니까
    for i in range(K - 1, 0, -1):
        for j in range(1, K + 1):
            if dp[i][j] == 0 and i < j:
                dp[i][j] = min(dp[i][k] + dp[k + 1][j] for k in range(i, j))
                # 마지막에는 전체 합 더해주기
                dp[i][j] += sum(arr[i - 1:j])
                

    print(dp)