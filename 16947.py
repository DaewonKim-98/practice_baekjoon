import sys
from collections import deque
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def findCircle(start, i, arr):
    for j in link[i]:
        if visited[j] == 0:
            visited[j] = 1
            findCircle(start, j, arr + [j])

        # 순환해서 처음에 방문했으면 순환선이므로
        if j == start and len(arr) > 2:
            for j in arr:
                circle[j] = 1
                
def findDistance(i):
    q = deque()
    visited = [0] * (N + 1)
    q.append(i)
    visited[i] = 1
    
    while q:
        station = q.popleft()
        
        # 순환선에 도착하면
        if circle[station] == 1:
            print(visited[station] - 1, end=' ')
            return

        for j in link[station]:
            if visited[j] == 0:
                visited[j] = visited[station] + 1
                q.append(j)
                
N = int(input().strip())
link = [set() for _ in range(N + 1)]
for _ in range(N):
    a, b = map(int, input().strip().split())
    link[a].add(b)
    link[b].add(a)
    
# 순환선 찾기
circle = [0] * (N + 1)
for i in range(1, N + 1):
    visited = [0] * (N + 1)
    if circle[i] == 0:
        visited[i] = 1
        findCircle(i, i, [i])

# 순환선 모두 찾았으면 거리찾기
for i in range(1, N + 1):
    if circle[i] == 1:
        print(0, end=' ')
    else:
        findDistance(i)