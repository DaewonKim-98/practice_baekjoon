dir = [[-1, 1], [0, 1], [1, 1]]

def dfs(r, c):
    global arrive
    global cnt
    # 마지막에 도착한다면
    if c == C - 1:
        arrive = True
        cnt += 1
        return
    for d in dir:
        nr, nc = r + d[0], c + d[1]
        if 0 <= nr < R and 0 <= nc < C and visited[nr][nc] == 0 and arr[nr][nc] == '.':
            visited[nr][nc] = 1
            dfs(nr, nc)
            if arrive == True:
                return


R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]

# 오른쪽위, 오른쪽, 오른쪽 아래 순으로 가는 dfs를 통해 위에서부터 시작해서 끝에 도착하는 것들이 있으면
# 그것이 최대 개수를 구할 수 있는 파이프라인인 것이므로 visited를 표시하고 다음으로 넘어가기
# 갓정식의 힌트
cnt = 0
visited = [[0] * C for _ in range(R)]
for r in range(R):
    arrive = False
    dfs(r, 0)

print(cnt)