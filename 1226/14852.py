N = int(input())

dp = [0] * 1000001
sum_dp = [0] * 1000001
dp[1] = 2
dp[2] = 7
dp[3] = 22
sum_dp[1] = dp[1]
# 3개일 때 2개짜리가 교차되는거도 생각
# 아 이게 그냥 교차되는게 앞에서부터 쭉 교차될수도 있으니까 모든 dp를 다 생각해야하네
# 시간초과나네 새로 sum_dp를 만들어서 앞에서부터의 dp 합들 넣기
for i in range(2, N + 1):
    if 3 < i:
        dp[i] = (2 * dp[i - 1] + 3 * dp[i - 2] + 2 * sum_dp[i - 3] + 2) % 1000000007
    sum_dp[i] += sum_dp[i - 1] + dp[i]
    
print(dp[N])