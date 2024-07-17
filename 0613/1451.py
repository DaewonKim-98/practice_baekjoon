N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

# 가로 / 세로 / 가로2 세로1 / 가로1 세로2 로 나누는 방법들
# 일단 누적합
for r in range(1, N):
    arr[r][0] += arr[r - 1][0]
for c in range(1, M):
    arr[0][c] += arr[0][c - 1]
for r in range(1, N):
    for c in range(1, M):
        arr[r][c] += arr[r - 1][c] + arr[r][c - 1] - arr[r - 1][c - 1]

maxValue = 0
# 가로
for i in range(N - 1):
    for j in range(i + 1, N):
        maxValue = max(maxValue, arr[i][M- 1] * (arr[j][M- 1] - arr[i][M- 1]) * (arr[N - 1][M- 1] - arr[j][M- 1]))
# 세로
for i in range(M - 1):
    for j in range(i + 1, M):
        maxValue = max(maxValue, arr[N - 1][i] * (arr[N - 1][j] - arr[N - 1][i]) * (arr[N - 1][M - 1] - arr[N - 1][j]))
# 2 1
for i in range(N - 1):
    for j in range(M - 1):
        maxValue = max(maxValue, arr[i][j] * (arr[i][M - 1] - arr[i][j]) * (arr[N - 1][M - 1] - arr[i][M - 1]))
        maxValue = max(maxValue, arr[i][M - 1] * (arr[N - 1][j] - arr[i][j]) * (arr[N - 1][M - 1] - arr[i][M - 1] - (arr[N - 1][j] - arr[i][j])))
        maxValue = max(maxValue, arr[i][j] * (arr[N - 1][j] - arr[i][j]) * (arr[N - 1][M - 1] - arr[N - 1][j]))
        maxValue = max(maxValue, arr[N - 1][j] * (arr[i][M - 1] - arr[i][j]) * (arr[N - 1][M - 1] - arr[N - 1][j] - (arr[i][M - 1] - arr[i][j])))

print(maxValue)