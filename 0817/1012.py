import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

T = int(input().strip())

# dfs 함수
def dfs(r, c):
    arr[r][c] = 0

    for d in dir:
        nr, nc = r + d[0], c + d[1]
        if 0 <= nr < N and 0 <= nc < M:
            if arr[nr][nc] == 1:
                dfs(nr, nc)
    

for case in range(1, T + 1):
    M, N, K = map(int, input().split())
    jirung = []
    for i in range(K):
        jirung.append(list(map(int, input().split())))

    # 0 배열
    arr = [[0] * M for _ in range(N)]
    # 1 넣기
    for r in range(N):
        for c in range(M):
            for j in jirung:
                if c == j[0] and r == j[1]:
                    arr[r][c] = 1

    # 상하좌우
    dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    # 배열을 돌면서 dfs 함수로 연결되는 모든 부분을 0으로 만들어준다.
    cnt = 0
    # 델타 탐색
    for r in range(N):
        for c in range(M):
            # 새로운 1이 나타나면 count 해준다.
            if arr[r][c] == 1:
                dfs(r, c)
                cnt += 1
    print(cnt)