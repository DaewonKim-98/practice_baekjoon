import sys
input = sys.stdin.readline

# 그냥 하던대로 합을 구하면 시간초과가 나서 누적합으로 구해야 한다.
n, m = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]
# 누적합을 구하기 위해 dp를 새로 둠
dp = [[0]*(m+1) for _ in range(n+1)]

# 누적합을 구하는 것으로 누적합의 행은 0부터 시작하며 구하는 배열의 좌표에서 누적합 좌표의
# 왼쪽, 위를 더하는데 그렇게 되면 대각선의 누적합이 중복이 되므로 빼준다.
for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = li[i-1][j-1] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]

# 구해야 하는 것은 i,j 에서 x, y까지의 누적합이므로  x,y 의 누적합에서 j 바로 이전, i 바로 이전의
# 누적합을 빼주고 중복해서 빠진 i와 j 모두의 이전 누적합을 더해준다.
k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    print(dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1])