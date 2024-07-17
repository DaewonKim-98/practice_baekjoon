import sys
input = sys.stdin.readline

M, N = map(int, input().strip().split())
arr = [[1] * M for _ in range(M)]
dir = [[-1, 0], [0, -1], [-1, -1]]
grow = [0] * (M * 2 - 1)

# N일 동안 에벌레 크기 변화
for _ in range(N):
    a, b, c = map(int, input().strip().split())
    # 아래부터 오른쪽까지 a, b, c만큼 자라기
    for i in range(a, a + b):
        grow[i] += 1
    for j in range(a + b, M * 2 - 1):
        grow[j] += 2
        
# grow만큼 자라게 하기
for i in range(M):
    arr[M - i - 1][0] += grow[i]
for j in range(1, M):
    arr[0][j] += grow[M + j - 1]
    
# 왼, 위, 왼위의 최댓값만큼 자라기
for r in range(1, M):
    for c in range(1, M):
        maxValue = 0
        for d in dir:
            nr, nc = r + d[0], c + d[1]
            maxValue = max(maxValue, arr[nr][nc])
            
        arr[r][c] = maxValue

for r in range(M):
    for c in range(M):
        print(arr[r][c], end=' ')
    print()