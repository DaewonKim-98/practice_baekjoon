import sys
input = sys.stdin.readline

a = [0] + list(input().strip())
b = [0] + list(input().strip())

dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i] == b[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            
max_length = 0
for lst in dp:
    max_length = max(max_length, max(lst))

print(max_length)