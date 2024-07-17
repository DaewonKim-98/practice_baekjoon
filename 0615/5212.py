R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
dir = [[0, 1], [1, 0], [-1, 0], [0, -1]]

narr = [['.'] * C for _ in range(R)]
# 땅의 좌표 저장해서 나중에 땅만 출력하도록
a = []
b = []

for r in range(R):
    for c in range(C):
        if arr[r][c] == 'X':
            sea = 0
            for d in dir:
                nr, nc = r + d[0], c + d[1]
                if 0 <= nr < R and 0 <= nc < C:
                    if arr[nr][nc] == '.':
                        sea += 1
                else:
                    sea += 1
            # 바다가 3명 혹은 4면이 아니면 그대로 땅이므로
            if sea < 3:
                narr[r][c] = 'X'
                a.append(r)
                b.append(c)
# print(narr,a,b)                
for r in range(min(a), max(a) + 1):
    for c in range(min(b), max(b) + 1):
        print(narr[r][c], end='')
    print()