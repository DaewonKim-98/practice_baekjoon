import sys
input = sys.stdin.readline

M, N = map(int, input().strip().split())
K = int(input().strip())
arr = [list(input().strip()) for _ in range(M)]

# 정글, 바다, 얼음의 개수를 각각 누적합으로 다 해두기
jungle = [[0] * (N + 1) for _ in range(M + 1)]
ocean = [[0] * (N + 1) for _ in range(M + 1)]
ice = [[0] * (N + 1) for _ in range(M + 1)]

for r in range(1, M + 1):
    for c in range(1, N + 1):
        if arr[r - 1][c - 1] == 'J':
            jungle[r][c] += 1
        jungle[r][c] += jungle[r - 1][c] + jungle[r][c - 1] - jungle[r - 1][c - 1]
        if arr[r - 1][c - 1] == 'O':
            ocean[r][c] += 1
        ocean[r][c] += ocean[r - 1][c] + ocean[r][c - 1] - ocean[r - 1][c - 1]
        if arr[r - 1][c - 1] == 'I':
            ice[r][c] += 1
        ice[r][c] += ice[r - 1][c] + ice[r][c - 1] - ice[r - 1][c - 1]
        
for _ in range(K):
    a, b, c, d = map(int, input().strip().split())
    j = jungle[c][d] - jungle[c][b - 1] - jungle[a - 1][d] + jungle[a - 1][b - 1]
    o = ocean[c][d] - ocean[c][b - 1] - ocean[a - 1][d] + ocean[a - 1][b - 1]
    i = ice[c][d] - ice[c][b - 1] - ice[a - 1][d] + ice[a - 1][b - 1]
    print(j, o, i)