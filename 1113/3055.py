from collections import deque

dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def bfs(r, c, water_q):
    # 고슴도치 큐
    go_q = []
    go_q.append((r, c, 0))
    # 물 큐
    water_q = water_q
    
    while go_q:
        go = go_q[:]
        go_q = []
        water = water_q[:]
        water_q = []
        # 물 먼저 움직이기
        while water:
            a, b = water.pop(0)
            for d in dir:
                na, nb = a + d[0], b + d[1]
                if 0 <= na < R and 0 <= nb < C and (arr[na][nb] != 'X' and arr[na][nb] != 'D' and arr[na][nb] != '*'):
                    arr[na][nb] = '*'
                    water_q.append((na, nb))

        # 물 움직였으면 고슴도치 움직이기
        while go:
            r, c, cnt = go.pop(0)
            for d in dir:
                nr, nc = r + d[0], c + d[1]
                if 0 <= nr < R and 0 <= nc < C and (arr[nr][nc] == '.' or arr[nr][nc] == 'D'):
                    # 굴에 도착했으면
                    if arr[nr][nc] == 'D':
                        print(cnt + 1)
                        exit()
                    arr[nr][nc] = cnt + 1
                    go_q.append((nr, nc, cnt + 1))


R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]

# bfs를 통해 물을 확장하고 고슴도치가 S로 가는 길 찾기
min_time = 2500
a, b = 0, 0
# 물 큐
water_q = []
for r in range(R):
    for c in range(C):
        if arr[r][c] == 'S':
            arr[r][c] = 0
            a, b = r, c
        elif arr[r][c] == '*':
            water_q.append((r, c))

bfs(a, b, water_q)
# 끝까지 다 돌았으면 이동할 수 없다는 것이므로
print('KAKTUS')