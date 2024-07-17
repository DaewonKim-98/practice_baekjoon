N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort()

# dp[i]는 i일째 최대 받을 수 있는 점수
dp = [0] * 1001

for i in range(N):
    for j in range(1000, 0, -1):
        if arr[i][0] >= j:
            dp[j] = max(dp[j], dp[j - 1] + arr[i][1])
            
print(max(dp))