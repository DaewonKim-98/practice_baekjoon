R, C, N = map(int, input().split())
arr = [list(input()) for _ in range(R)]

# 처음 폭탄을 놓고 1초 동안은 아무것도 하지 않으므로
for r in range(R):
    for c in range(C):
        if arr[r][c] == 'O':
            arr[r][c] = 1
            
dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            
for _ in range(1, N):
    # 폭탄 설치 된 곳 + 1
    # 폭탄 설치 안된 곳 폭탄 설치
    for r in range(R):
        for c in range(C):
            if arr[r][c] != '.':
                arr[r][c] += 1
            else:
                arr[r][c] = 0
    
    # 3초 되면 주위 다 터뜨리기
    for r in range(R):
        for c in range(C):
            if arr[r][c] == 3:
                arr[r][c] = '.'
                for d in dir:
                    nr, nc = r + d[0], c + d[1]
                    if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] != 3:
                        arr[nr][nc] = '.'
    # print(arr)                
for r in range(R):
    for c in range(C):
        state = '.'
        if arr[r][c] != '.':
            state = 'O'
        print(state, end='')
    print()