import sys
input = sys.stdin.readline

T = int(input().strip())
for case in range(1, T + 1):
  N = int(input().strip())
  arr = list(map(int, input().strip().split()))
  M = int(input().strip())
  
  # dp[i]는 i원을 만드는 경우의 수
  dp = [0] * (M + 1)
  for j in range(N):
    if arr[j] < M + 1:
      dp[arr[j]] += 1
    for i in range(arr[j], M + 1):
      # 이전 것이 존재한다면 더할 수 있다는 것이므로
      if i - arr[j] > 0 and dp[i - arr[j]] != 0:
        dp[i] += dp[i - arr[j]]
  # print(dp)    
  print(dp[M])