import sys
input = sys.stdin.readline

N = int(input().strip())
arr = [0] + list(map(int, input().strip().split()))

# dp i개를 갖기 위해 지불해야 하는 금액의 최댓값
dp = [0] * (N + 1)
dp[1] = arr[1]

for i in range(2, N + 1):
    # i - j번째에서 arr[j]를 더한 것과 비교해서 최댓값 찾기
    for j in range(i, 0, -1):
        dp[i] = max(dp[i], dp[i - j] + arr[j])
        
print(dp[N])