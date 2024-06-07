N = int(input())
dp = [0] * (31)
dp[1] = 0
dp[2] = 3
dp[0] = 1
# 홀수는 안됨
# 아 그냥 더 이전에서도 올 수 있으니까 앞에꺼 쭉 더해줘야 함
for i in range(4, 31, 2):
    dp[i] = dp[i - 2] * 3
    for j in range(0, i - 4 + 1, 2):
        dp[i] += dp[j] * 2
    
print(dp[N])