N = int(input())
arr = list(map(int, input().split()))

# 앞에서부터 확인 + 뒤에서부터 확인으로 두개의 dp를 만들어 최댓값 찾기
stoe_dp = [1] * N
etos_dp = [1] * N
max_length = 0

# 앞에서부터 확인
for i in range(N):
    for j in range(i):
        if arr[j] < arr[i]:
            stoe_dp[i] = max(stoe_dp[j] + 1, stoe_dp[i])

# 뒤에서부터 확인
for i in range(N - 1, -1, -1):
    for j in range(N - 1, i, -1):
        if arr[j] < arr[i]:
            etos_dp[i] = max(etos_dp[j] + 1, etos_dp[i])
    

# dp를 돌면서 최댓값 갱신
for i in range(N):
    length = stoe_dp[i] + etos_dp[i] - 1 
    max_length = max(max_length, length)

print(max_length)