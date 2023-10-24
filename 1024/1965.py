N = int(input())
arr = list(map(int, input().split()))

# 넣을 수 있는 상자의 개수를 dp로
dp = [1] * N

# 처음부터 시작해 끝까지 탐색했을 때 점점 커지면 dp 추가?
# dp는 앞에서부터 탐색해서 자기보다 작으면 1을 추가하는 식으로 하면 자기보다 작은 것들에 대해 1씩
# 추가되는 것이므로 최대의 상자 개수를 출력할 수 있을 것인가!?!! 젠장 틀렸네
# 이미 자기가 더 큰 값을 가지고 있으면 바꿀 필요 없으므로 max로 추가
for i in range(N - 1):
    for j in range(i + 1, N):
        if arr[i] < arr[j]:
            dp[j] = max(dp[i] + 1, dp[j])

print(max(dp))