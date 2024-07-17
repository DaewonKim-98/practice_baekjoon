from collections import deque

dir = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

def bong(r, c):
    q = deque()
    q.append((r, c))
    visited[r][c] = 1
    height = arr[r][c]
    isBong = True
    
    while q:
        r, c = q.popleft()
        for d in dir:
            nr, nc = r + d[0], c + d[1]
            if 0 <= nr < N and 0 <= nc < M:
                # 높이가 같은 집합들 찾기
                if arr[nr][nc] == height and visited[nr][nc] == 0:
                    q.append((nr, nc))
                    visited[nr][nc] = 1
                # 주위가 자기보다 큰게 있으면 산봉우리가 아니므로
                elif arr[nr][nc] > height:
                    isBong = False
    
    # 산봉우린지 판단
    if isBong:
        return True
    else:
        return False

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 인접하면서 높이가 같은 집합들 찾고 이제 그것들 주위가 다 자기보다 작은지 체크
visited = [[0] * M for _ in range(N)]
cnt = 0
for r in range(N):
    for c in range(M):
        if arr[r][c] != 0 and visited[r][c] == 0:
            if bong(r, c):
                cnt += 1
            
print(cnt)