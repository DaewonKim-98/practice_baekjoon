import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

# 합의 최댓값
max_sum = 0
for i in range(N - K + 1):
    sum_tem = 0
    for j in range(i, i + K):
        sum_tem += arr[j]
    if max_sum < sum_tem:
        max_sum = sum_tem

print(max_sum)