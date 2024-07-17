import sys
import heapq
input = sys.stdin.readline

def getTime(a):
    q = []
    visited = [0] * (N + 1)
    heapq.heapify(q)
    heapq.heappush(q, (0, a))
    
    while q:
        time, partyHall = heapq.heappop(q)
        
        if visited[partyHall] == 0:
            fastTime[a][partyHall] = time
            visited[partyHall] = 1
            for j in link[partyHall]:
                if visited[j[0]] == 0:
                    heapq.heappush(q, (time + j[1], j[0]))

N, M = map(int, input().strip().split())
link = [[] for _ in range(N + 1)]
for i in range(N):
    arr = list(map(int, input().strip().split()))
    for j in range(N):
        if i != j:
            link[i + 1].append((j + 1, arr[j]))

# 걍 빠른 길 미리 찾아두기
fastTime = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    getTime(i)

for _ in range(M):
    a, b, c = map(int, input().strip().split())
    if fastTime[a][b] <= c:
        print('Enjoy other party')
    else:
        print('Stay here')