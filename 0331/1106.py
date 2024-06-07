C, N = map(int, input().split())
# arr[i]는 i고객을 얻을 수 있는 비용
arr = [0] * 1101
for _ in range(N):
    a, b = map(int, input().split())
    if arr[b] != 0:
        arr[b] = min(arr[b], a)
    else: 
        arr[b] = a

# dp[i] 는 i고객을 얻을 수 있는 최소비용
dp = [100000] * 1101

for i in range(1, 1101):
    if arr[i] != 0:
        dp[i] = arr[i]
    for j in range(1, i):
        if arr[j] != 0:
            # j고객을 얻을 수 있는 비용이 있다면 i에서 뺀것에서 더해주기
            dp[i] = min(dp[i - j] + arr[j], dp[i])
        
# print(arr)        
# print(dp)
# C 이상인 것에서 최솟값
value = min(dp[C:])
print(value)