AN, AM = map(int, input().split())
Aarr = [list(map(int, input().split())) for _ in range(AN)]
BN, BM = map(int, input().split())
Barr = [list(map(int, input().split())) for _ in range(BN)]

arr = [[0] * BM for _ in range(AN)]

for r in range(AN):
    for c in range(BM):
        arr[r][c] = 0
        for i in range(AM):
            arr[r][c] += Aarr[r][i] * Barr[i][c]
            
for r in range(AN):
    for c in range(BM):
        print(arr[r][c], end=' ')
    print()