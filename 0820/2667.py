import sys
input = sys.stdin.readline

N = int(input().strip())
arr = [list(map(int, input().strip())) for _ in range(N)]

# 방향을 나타내는 dir
dir = [[0, -1], [-1, 0], [0, 1], [1, 0]]

# 단지를 나타내는 연결된 1들을 찾는 bfs
def bfs(N, r, c):
    visited = [[0] * (N + 1) for _ in range(N)]
    visited[r][c] = 1
    q = [[r, c]]
    # 단지내 집의 수
    house = 1
    
    while len(q) > 0:
        [r, c] = q.pop(0)
        for d in dir:
            nr, nc = r + d[0], c + d[1]
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] == 1 and visited[nr][nc] == 0:
                    q.append([nr, nc])
                    visited[nr][nc] = 1
                    # 나중에 탐색할 때 연결된 부분은 탐색하지 않기 위해
                    arr[nr][nc] = 0
                    # 단지내 집의 수에 1 추가
                    house += 1
    return house
                    

# 단지 리스트
a_complex = []
# 배열을 돌면서 탐색                 
for r in range(N):
    for c in range(N):
        if arr[r][c] == 1:
            a_complex.append(bfs(N, r, c))
            
print(len(a_complex))
a_complex.sort()
for i in a_complex:
    print(i)