from itertools import combinations
from collections import deque

def bfs(r, c):
    q = deque()
    q.append((r, c))
    visited = [[0] * 5 for _ in range(5)]
    visited[r][c] = 1
    cnt = 1
    while q:
        r, c = q.popleft()
        if cnt == 7:
            return True
        for d in dir:
            nr, nc = r + d[0], c + d[1]
            if 0 <= nr < 5 and 0 <= nc < 5 and visited[nr][nc] == 0:
                if (nr, nc) in com:
                    q.append((nr, nc))
                    visited[nr][nc] = 1
                    cnt += 1
    if cnt == 7:
        return True
    else:
        return False

arr = [list(input()) for _ in range(5)]
students = []
for r in range(5):
    for c in range(5):
        students.append((r, c))
        
# 7개로 된 학생 집합에서 연결된 것중에 7공주 찾기
comStudents = combinations(students, 7)

dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
cnt = 0
for com in comStudents:
    # 연결되었는지 판단
    isLinked = bfs(com[0][0], com[0][1])
    if isLinked:
        som = 0
        for i in com:
            if arr[i[0]][i[1]] == 'S':
                som += 1
        if som >= 4:
            cnt += 1
            
print(cnt)