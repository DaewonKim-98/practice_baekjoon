N, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: [x[0], -x[1]])

# dp[i]는 i시간동안 공부했을 때 얻을 수 있는 최대 점수
dp = [0] * (T + 1)
for j in arr:
    for i in range(T, 0, -1):
        # 시간이 된다면
        if j[0] <= i:
            dp[i] = max(dp[i], dp[i - j[0]] + j[1])
# print(dp)          
print(dp[T])