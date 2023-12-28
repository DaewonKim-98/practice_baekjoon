R, C, W = map(int, input().split())

paskal = [[1] * i for i in range(1, 31)]
for r in range(2, 30):
    for c in range(1, r):
        paskal[r][c] = paskal[r - 1][c - 1] + paskal[r - 1][c]

result = 0 
for i in range(W):
    for j in range(i + 1):
        result += paskal[R - 1 + i][C - 1 + j]
        
print(result)