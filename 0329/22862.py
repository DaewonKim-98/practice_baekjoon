N, K = map(int, input().split())
arr = list(map(int, input().split()))

# dp[i][j]는 i번째 j개를 삭제한 수열에서 가장 긴 길이
dp = [[0] * (K + 1) for _ in range(N)]

if arr[0] % 2 == 0:
  dp[0][0] = 1
  
for i in range(1, N):
  for j in range(0, i):
    if arr[j] % 2 == 1