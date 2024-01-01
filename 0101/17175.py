N = int(input())

#아 이거 dp네 알미ㅏㅇ;너라ㅣㅜ미ㅏㅇㄴ리마눙ㄹ
dp = [0] * (N + 1)
if N == 0:
    print(1)
    exit()
dp[1] = 1

if N > 1:
    dp[2] = 3
    # 맨 처음 자기 호출 + 1
    for i in range(3, N + 1):
        dp[i] = (dp[i - 2] + dp[i - 1] + 1) % 1000000007
        
print(dp[N])