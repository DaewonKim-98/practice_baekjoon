import sys
input = sys.stdin.readline

# 나이트의 이동할 수 있는 방향
move_knight = [[2, 1], [1, 2], [-1, -2], [-2, -1], [-2, 1], [-1, 2], [1, -2], [2, -1]]

# 최소 탐색으로 나이트의 칸을 찾아야 하므로
def bfs(l, S, G):
    visited = [[0] * (l + 1) for _ in range(l + 1)]
    visited[S[0]][S[1]] = 1
    q = [S]

    while len(q) > 0:
        [r, c] = q.pop(0)
        # 나이트가 도착점에 도착하면 출력
        if [r, c] == G:
            return visited[r][c] - 1
        for d in move_knight:
            nr, nc = r + d[0], c + d[1]
            # 이동한 나이트는 체스판 안에 있어야 하므로
            if 0 <= nr < l and 0 <= nc < l and visited[nr][nc] == 0:
                visited[nr][nc] = visited[r][c] + 1
                q.append([nr, nc])

T = int(input().strip())
for case in range(1, T + 1):
    l = int(input().strip())
    S = list(map(int, input().split()))
    G = list(map(int, input().split()))

    print(bfs(l, S, G))