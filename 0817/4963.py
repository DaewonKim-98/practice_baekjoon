import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(r, c):
    arr[r][c] = 0

    # 델타 탐색을 위한 방향 - 대각선까지 모두 포함
    dir = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]

    # 델타 탐색으로 재귀로 섬을 0으로 모두 바꾸어준다.
    for d in dir:
        nr, nc = r + d[0], c + d[1]
        if 0 <= nr < h and 0 <= nc < w:
            if arr[nr][nc] == 1:
                dfs(nr, nc)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    arr = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0
    for r in range(h):
        for c in range(w):
            # 돌릴 때 연결된 섬인 부분을 모두 지우고 개수를 새준다.
            if arr[r][c] == 1:
                dfs(r, c)
                cnt += 1
    
    print(cnt)