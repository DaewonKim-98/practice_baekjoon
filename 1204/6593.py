from collections import deque

# 3차원 동서남북상하
dir = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]

# bfs
def bfs(l, r, c):
    visited = [[[0] * C for _ in range(R)] for _ in range(L)]
    q = deque()
    visited[l][r][c] = 1
    q.append([l, r , c])
    
    while q:
        # print(q)
        l, r, c = q.popleft()
        if arr[l][r][c] == 'E':
            print(f'Escaped in {visited[l][r][c] - 1} minute(s).')
            return

        for d in dir:
            nl, nr, nc = l + d[0], r + d[1], c + d[2]
            if 0 <= nl < L and 0 <= nr < R and 0 <= nc < C and visited[nl][nr][nc] == 0 and arr[nl][nr][nc] != '#':
                visited[nl][nr][nc] = visited[l][r][c] + 1
                q.append([nl, nr, nc])
                
    # while문을 다 돌았어도 안끝났으면 탈출 불가능이므로
    print('Trapped!')
    return


while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break

    # 층 먼저
    arr = []
    for _ in range(L):
        floor = [list(input()) for _ in range(R)]
        arr.append(floor)
        input()
    
    # print(arr)
    for l in range(L):
        for r in range(R):
            for c in range(C):
                if arr[l][r][c] == 'S':
                    bfs(l, r, c)