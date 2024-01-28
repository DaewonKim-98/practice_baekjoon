N, M = map(int, input().split())
queen = list(map(int, input().split()))
knight = list(map(int, input().split()))
pawn = list(map(int, input().split()))

arr = [[0] * M for _ in range(N)]
# 기물 놓기
for i in range(queen[0]):
    arr[queen[1 + 2 * i] - 1][queen[1 + 2 * i + 1] - 1] = 'q'
for i in range(knight[0]):
    arr[knight[1 + 2 * i] - 1][knight[1 + 2 * i + 1] - 1] = 'k'
for i in range(pawn[0]):
    arr[pawn[1 + 2 * i] - 1][pawn[1 + 2 * i + 1] - 1] = 'p'
  
# dir
qdir = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
kdir = [[2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2], [1, 2]]

# 돌면서 갈 수 있는 곳 표시
for r in range(N):
    for c in range(M):
        # 퀸
        if arr[r][c] == 'q':
            for q in qdir:
                i = 0
                # 막히거나 끝까지
                while True:
                    i += 1
                    nr, nc = r + q[0] * i, c + q[1] * i
                    if 0 <= nr < N and 0 <= nc < M and (arr[nr][nc] == 0 or arr[nr][nc] == 1):
                        arr[nr][nc] = 1
                    # 막히거나 끝이면
                    else:
                        break
                    
        # 나이트
        elif arr[r][c] == 'k':
            for k in kdir:
                nr, nc = r + k[0], c + k[1]
                if 0 <= nr < N and 0 <= nc < M and (arr[nr][nc] == 0 or arr[nr][nc] == 1):
                    arr[nr][nc] = 1
# print(arr)                   
# 다 돌았으면 안전한 칸 찾기
cnt = 0
for r in range(N):
    for c in range(M):
        if arr[r][c] == 0:
            cnt += 1
            
print(cnt)