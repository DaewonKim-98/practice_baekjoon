from copy import deepcopy

N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# N // 2, M // 2 만큼 돌리면서 반대 것들 돌리기
# 시간초과 없애려면 각 돌리는 횟수를 R에서 도는 개수만큼으로 나눈 나머지를 해야할듯
length = N * 2 + M * 2 - 4
# 돌려야되는 횟수
for i in range(min(N, M) // 2):
    for _ in range(R % length):
        lt, rt, lb, rb = arr[i][i], arr[i][M - 1 - i], arr[N - 1 - i][i], arr[N - 1 - i][M - 1 - i]
        # 순서대로
        for c in range(i, M - 1 - i):
            arr[i][c] = arr[i][c + 1]
        for r in range(i, N - 1 - i):
            arr[r][M - 1 - i] = arr[r + 1][M - 1 - i]
        for c in range(i, M - 1 - i):
            arr[N - 1 - i][M - 1 - c] = arr[N - 1 - i][M - 1 - c - 1]
        for r in range(i, N - 1 - i):
            arr[N - 1 - r][i] = arr[N - 1 - r - 1][i]
        arr[i + 1][i], arr[i][M - 1 - i - 1], arr[N - 1 - i][i + 1], arr[N - 1 - i - 1][M - 1 - i] = lt, rt, lb, rb
        # print(arr)
    length -= 8
    
for i in range(N):
    for j in range(M):
        print(arr[i][j], end=' ')
    print()