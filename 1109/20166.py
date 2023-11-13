from collections import deque
import sys
input = sys.stdin.readline

dir = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

# def pactorial(n):
#     mul = 1
#     for i in range(1, n + 1):
#         mul *= i
#     return mul

def bfs(r, c, string):
    global cnt
    q = deque()
    q.append((r, c, arr[r][c]))

    while q:
        r, c, s = q.popleft()
        # 문자열을 찾으면
        if s == string:
            # 더해주기
            cnt += 1
            continue
        
        for d in dir:
            nr, nc = r + d[0], c + d[1]
            # 주어진 배열을 넘어가면 반대쪽으로 넘어가므로
            if nr == -1:
                nr = N - 1
            elif nr == N:
                nr = 0
            if nc == -1:
                nc = M - 1
            elif nc == M:
                nc = 0
            # print(r, c, s, string)
            # print(s + arr[nr][nc], string[:len(s + arr[nr][nc])])
            if s + arr[nr][nc] == string[:len(s + arr[nr][nc])]:
                # visited[nr][nc] = 1
                q.append((nr, nc, s + arr[nr][nc]))

N, M, K = map(int, input().split())
arr = [list(input().strip()) for _ in range(N)]
dic = {}

for _ in range(K):
    visited = [[0] * M for _ in range(N)]
    string = input().strip()
    if string in dic:
        print(dic[string])
    else:
        length = len(string)
        cnt = 0
        # bfs를 통해 문자열을 찾고 bfs의 길이가 문자열을 넘어가면 더 이상 찾지 못하므로 return
        for r in range(N):
            for c in range(M):
                if arr[r][c] == string[0]:
                    bfs(r, c, string)
                    dic[string] = cnt

        print(cnt)