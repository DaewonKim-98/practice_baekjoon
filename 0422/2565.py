N = int(input())
arr = []
for _ in range(N):
  a, b = map(int, input().split())
  arr.append([a, b])
  
# 정렬한 다음 B부분이 증가하는 것들로 가장 길게 증가하는 것들을 찾고
# N에서 빼면 그게 최소로 삭제한 전깃줄 수
arr.sort()
dp = [1] * N

for i in range(1, N):
  for j in range(i + 1):
    if arr[j][1] < arr[i][1]:
      dp[i] = max(dp[j] + 1, dp[i])
      
print(N - max(dp))