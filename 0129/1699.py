# EASY BOY~
from math import sqrt

N = int(input())
dp = [0] + [10000] * N
dp[1] = 1
for i in range(2, N + 1):
    for j in range(1, int(sqrt(i)) + 1):
        # print(j)
        dp[i] = min(dp[i], dp[i - j ** 2] + 1)
        
print(dp[N])