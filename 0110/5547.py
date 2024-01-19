# 짝수행, 홀수행의 방향을 다르게
even_dir = [[0, 1], [1, 1], [1, 0], [0, -1], [-1, 0], [-1, 1]]
odd_dir = [[-1, -1], [-1, 0], [0, 1], [1, 0], [1, -1], [0, -1]]

def bfs(r, c):
    global wall
    q = []
    q.append([r, c])
    visited[r][c] = 1
    # 밖이랑 연결되어 있는지 판단
    link_out = False
    # 벽과 만나는 개수
    meet_wall = 0
    
    while q:
        r, c = q.pop(0)
        
        if r % 2 == 0:
            dir = even_dir
        else:
            dir = odd_dir
            
        for d in dir:
            nr, nc = r + d[0], c + d[1]
            # 밖이랑 연결되면
            if nr == -1 or nr == H or nc == -1 or nc == W:
                link_out = True
                continue
            # 밖과 연결되지 않고 방문하지 않았으면
            if visited[nr][nc] == 0:
                # 건물과 만나면 1 추가
                if arr[nr][nc] == 1:
                    meet_wall += 1
                    continue
                # 연결된 길로 q에 추가
                elif arr[nr][nc] == 0:
                    q.append([nr, nc])
                    visited[nr][nc] = 1
    
    # 다 돌았을 때 밖과 연결된 부분이면 밖에서 보이는 벽인 것이므로
    if link_out == True:
        wall += meet_wall
        return

W, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(H)]
wall = 0

# 0에서 1인 부분을 만나면 벽이므로 1을 더해주는데 0을 bfs로 찾아 돌았을 때
# 밖이랑 연결되어 있지 않은 부분이면 건물 안에 있는 곳이므로 더해주지 않는다.
visited = [[0] * W for _ in range(H)]
for r in range(H):
    for c in range(W):
        if visited[r][c] == 0 and arr[r][c] == 0:
            bfs(r, c)
        
        # 건물이 가장 바깥에 있는 경우도 따로 계산
        if arr[r][c] == 1:
            if r % 2 == 0:
                dir = even_dir
            else:
                dir = odd_dir  
                
            for d in dir:
                nr, nc = r + d[0], c + d[1]
                # 밖이랑 연결된 부분이 벽이므로
                if nr == -1 or nr == H or nc == -1 or nc == W:
                    wall += 1

print(wall)