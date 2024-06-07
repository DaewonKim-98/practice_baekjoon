N = int(input())
arr = list(map(int, input().split()))

# dp[i] 는 i번째에서 최대로 제시할 수 있는 개수
dp = [1] * N
for i in range(1, N):
  # 이전 것들과 비교
  for j in range(i):
    # i번째가 j보다 크면 j번째에서 계속 갱신
    if arr[i] > arr[j]:
      dp[i] = max(dp[i], dp[j] + 1)

# print(dp)
print(max(dp))