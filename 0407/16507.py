import sys
input = sys.stdin.readline

R, C, Q = map(int, input().strip().split())
arr = [list(map(int, input().strip().split())) for _ in range(R)]

# 누적합
arrSum = [[0] * (C + 1) for _ in range(R + 1)]
for r in range(1, R + 1):
    for c in range(1, C + 1):
        arrSum[r][c] = arrSum[r - 1][c] + arrSum[r][c - 1] - arrSum[r - 1][c - 1] + arr[r - 1][c - 1]
# print(arrSum)        
for _ in range(Q):
    r1, c1, r2, c2 = map(int, input().strip().split())
    print((arrSum[r2][c2] - arrSum[r1 - 1][c2] - arrSum[r2][c1 - 1] + arrSum[r1 - 1][c1 - 1]) // ((r2 - r1 + 1) * (c2 - c1 + 1)))