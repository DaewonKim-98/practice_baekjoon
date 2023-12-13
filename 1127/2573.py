from copy import deepcopy
from collections import deque

dir = [[0, 1], [0, -1], [-1, 0], [1, 0]]

def bfs(r, c):
    q = deque()
    q.append([r, c])
    visited[r][c] = 1
    
    while q:
        r, c = q.popleft()
        for d in dir:
            nr, nc = r + d[0], c + d[1]
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] != 0 and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                q.append([nr, nc])


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 빙산이 녹기 전 배열을 설정해두고 이배열을 돌면서 arr 수정
copy_arr = deepcopy(arr)

# 빙산이 2개 이상으로 분리될 때까지
year = 1
while True:
    cnt = 0
    visited = [[0] * M for _ in range(N)]
    # 빙산이 모두 다 녹은지 아닌지 판단
    all_melt = True
    for r in range(N):
        for c in range(M):
            # 빙산이 있으면
            if arr[r][c] != 0:
                for d in dir:
                    nr, nc = r + d[0], c + d[1]
                    if 0 <= nr < N and 0 <= nc < M and copy_arr[nr][nc] == 0 and arr[r][c] > 0:
                        arr[r][c] -= 1
            
            # 다 녹이고도 빙산이 남아 있으면
            if arr[r][c] != 0:
                # 빙산이 남아있다 표시
                all_melt = False
    
    # 한번에 빙산이 모두 다 녹았으면
    if all_melt == True:
        print(0)
        exit()
        
    # 빙산이 남아있고 다 녹지 않았으면 연결되어있는지 확인
    visited = [[0] * M for _ in range(N)]
    for r in range(N):
        for c in range(M):
            if arr[r][c] != 0 and visited[r][c] == 0:
                cnt += 1
                bfs(r, c)
            if cnt > 1:
                print(year)
                exit()
                
                
    copy_arr = deepcopy(arr)
    year += 1
                
    