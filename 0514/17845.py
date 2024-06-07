N, K = map(int, input().split())
subjects = []
for _ in range(K):
    i, t = map(int, input().split())
    subjects.append((t, i))
    
subjects.sort(key=lambda x: [x[0], -x[1]])

# dp[i]는 i공부시간동안 최대 중요도
dp = [0] * (N + 1)

for j in range(K):
    for i in range(N, 0, -1):
        if subjects[j][0] <= i:
            dp[i] = max(dp[i], dp[i - subjects[j][0]] + subjects[j][1])
            
print(dp[N])