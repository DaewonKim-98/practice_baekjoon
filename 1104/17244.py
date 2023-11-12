from itertools import permutations

dir = [[0, 1], [1, 0], [-1, 0], [0, -1]]

def bfs(lst1, lst2):
    visited = [[0] * N for _ in range(M)]
    q = []
    visited[lst1[0]][lst1[1]] = 1
    q.append((lst1[0], lst1[1]))

    while q:
        r, c = q.pop(0)
        # 다음 물건에 도착하면
        if r == lst2[0] and c == lst2[1]:
            return visited[r][c] - 1
        for d in dir:
            nr, nc = r + d[0], c + d[1]
            if 0 <= nr < M and 0 <= nc < N and visited[nr][nc] == 0 and arr[nr][nc] != '#':
                q.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1

N, M = map(int, input().split())
arr = []

# 챙겨야 하는 물건의 개수
things = 0
for _ in range(M):
    lst = list(input())
    things += lst.count('X')
    arr.append(lst)

# 문에서 가장 가까운 X부터 시작해서 다음 X, 다음 찾는 식으로 역으로 X 찾아나가기?
# 걍 안되는듯 ㅋㅋ 모든 X를 순열로 나열한 뒤 그 사이의 거리를 bfs로 찾고
# 모든 경우에서 최솟값 찾기?
e = ()
s = ()
x = []
for r in range(M):
    for c in range(N):
        if arr[r][c] == 'E':
            e = (r ,c)
        elif arr[r][c] == 'S':
            s = (r, c)
        elif arr[r][c] == 'X':
            x.append((r, c))

# x를 순열로 돌리면
x = permutations(x, things)
min_time = 100000
for lst in list(x):
    lst = [s] + list(lst) + [e]
    time = 0
    for i in range(things + 1):
        time += bfs(lst[i], lst[i + 1])
        if time >= min_time:
            break
        
    min_time = min(time, min_time)

print(min_time)