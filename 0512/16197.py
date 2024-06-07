from collections import deque
from copy import deepcopy

def bfs(a, b, c, d):
    q = deque()
    q.append((a, b, c, d, 0))
    
    while q:
        a, b, c, d, cnt = q.popleft()
        if cnt >= 10:
            print(-1)
            return 
        for direction in dir:
            na, nb, nc, nd = a + direction[0], b + direction[1], c + direction[0], d + direction[1]
            # 안넘어가면 움직이기
            if 0 <= na < N and 0 <= nb < M and 0 <= nc < N and 0 <= nd < M:
                if arr[na][nb] != '#' and arr[nc][nd] != '#':
                    q.append((na, nb, nc, nd, cnt + 1))
                elif arr[na][nb] != '#':
                    q.append((na, nb, c, d, cnt + 1))
                elif arr[nc][nd] != '#':
                    q.append((a, b ,nc, nd, cnt + 1))
            # 둘 다 넘어가면 안되므로
            elif (not (0 <= na < N and 0 <= nb < M)) and (not (0 <= nc < N and 0 <= nd < M)):
                # print(na, nb, nc, nd)
                continue
            else:
                # print(na, nb, nc, nd)
                print(cnt + 1)
                return
    print(-1)

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

a, b, c, d = 0, 0, 0, 0
first = True
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'o':
            if first == True:
                a, b = i, j
            else:
                c, d = i, j
            first = False

dir = [[0, 1], [0, -1], [-1, 0], [1, 0]]

# bfs를 통해
# print(a, b, c, d)
bfs(a, b, c, d)