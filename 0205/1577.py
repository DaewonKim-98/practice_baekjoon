<<<<<<< HEAD
# 아진짜 개뻘짓 dp였네 어쩐지 절대 안되더라 ㅁ니아러ㅗ미낭룸낭러ㅜㅁㄴ어ㅏㄻ
N, M = map(int, input().split())
K = int(input())

# 공사 중인 도로
construction = set()
for _ in range(K):
    construction.add(tuple(map(int, input().split())))

dp = [[0] * (N + 1) for _ in range(M + 1)]

# 공사중이 아니면 쭉 dp
for i in range(1, M + 1):
    if (0, i - 1, 0, i) not in construction and (0, i, 0, i - 1) not in construction:
        dp[i][0] = 1
    else:
        break
        
for j in range(1, N + 1):
    if (j - 1, 0, j, 0) not in construction and (j, 0, j - 1, 0) not in construction:
        dp[0][j] = 1
    else:
        break

# print(dp)
# dp[i][j] 는 i,j로 가는 경우의 수
for i in range(1, M + 1):
    for j in range(1, N + 1):
        dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        # 공사중인 것이면 빼기
        if (j, i, j - 1, i) in construction or (j - 1, i, j, i) in construction:
            dp[i][j] -= dp[i][j - 1]
            
        if (j, i, j, i - 1) in construction or (j, i - 1, j, i) in construction:
            dp[i][j] -= dp[i - 1][j]
        
print(dp[M][N])
        
=======
N, M = map(int, input().split())
K = int(input())
>>>>>>> acda1e901b7adfec85929c2d085915debcc26fb8
