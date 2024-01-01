N = int(input())
arr = [1] + [float(input()) for _ in range(N)]

# [최댓값, 최댓값의 처음 인덱스]
dp = [[1, i] for i in range(N + 1)]

dp[1] = [arr[1], 1]

for i in range(2, N + 1):
    dp[i][0] *= arr[i]
    mul = arr[i]
    # 가장 뒤에서부터 시작해서 곱해가는데 더 크면 갱신
    for j in range(i - 1, dp[i - 1][1] - 1, -1):
        mul *= arr[j]
        if dp[i][0] < mul:
            dp[i][0] = mul
            dp[i][1] = j
            
    # 다 곱한게 이전 것보다 작으면 그냥 그걸로
    if dp[i][0] < dp[i - 1][0]:
        dp[i][0] = dp[i - 1][0]
        dp[i][1] = dp[i - 1][1]
        
# print(dp)
# print(round(dp[N][0], 3))
print(f'{dp[N][0]:.3f}')


# 쉽게 이렇게 하면 되네
# N = int(input())
# dp = [0] * (N + 1)

# for i in range(1, N + 1):
#     dp[i] = float(input())
#     dp[i] = max(dp[i], dp[i - 1] * dp[i])

# # print(dp)
# print(f'{max(dp):.3f}')