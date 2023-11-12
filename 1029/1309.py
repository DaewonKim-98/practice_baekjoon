N = int(input())

# N번째 열에 사자를 배치하는 경우의 수를 dp로 나타내기
dp = [0] * N
if N == 1:
    print(3)
elif N == 2:
    print(7)
else:
    dp[0] = 3
    dp[1] = 7

    # dp[i- 1]가 0 0이 되는 경우는 dp[i -2] 그 때는 dp[i]는 3배
    # 0 0이 되지 않는 경우는 dp[i - 1] - dp[i - 2]이므로 들어갈 경우는 2배
    for i in range(2, N):
        dp[i] = (dp[i  -2] * 3 + (dp[i - 1] - dp[i - 2]) * 2) % 9901
        
    print(dp[N - 1])

