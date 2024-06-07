import sys
from collections import deque
input = sys.stdin.readline

def bfs(i):
    visited = [0] * (N + 1)
    q = deque()
    visited[i] = 1
    q.append(i)
    cnt = 0
    
    # 가벼운 것들 개수
    while q:
        num = q.popleft()
        for j in lightLink[num]:
            if visited[j] == 0:
                q.append(j)
                visited[j] = 1
                cnt += 1
    # 무거운 것들 개수
    q.append(i)  
    while q:
        num = q.popleft()
        for j in heavyLink[num]:
            if visited[j] == 0:
                q.append(j)
                visited[j] = 1
                cnt += 1
    # 전체에서 결과 아는 것들 빼기
    print(N - 1 - cnt)

N = int(input().strip())
M = int(input().strip())
lightLink = [[] for _ in range(N + 1)]
heavyLink = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().strip().split())
    lightLink[a].append(b)
    heavyLink[b].append(a)
    
# bfs로 개수 찾아서 출력
for i in range(1, N + 1):
    bfs(i)
