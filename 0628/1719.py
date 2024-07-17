import sys
import heapq
input = sys.stdin.readline

def findNumber(i):
    q = []
    visited = [0] * (N + 1)
    heapq.heapify(q)
    heapq.heappush(q, (0, i, i))
    
    while q:
        t, number, j = heapq.heappop(q)
        # 방문하지 않았으면
        if visited[j] == 0:
            visited[j] = 1
            # i와 j가 같으면
            if i == j:
                time[i][j] = '-'
            # 다르면 i에서 j로 가는 바로 이전이 number이므로
            else:
                time[j][i] = number
            for k in link[j]:
                heapq.heappush(q, (k[0] + t, j, k[1]))

N, M = map(int, input().strip().split())
link = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().strip().split())
    link[a].append((c, b))
    link[b].append((c, a))
    
# 다이스트라로
time = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    findNumber(i)
            
for r in range(1, N + 1):
    for c in range(1, N + 1):
        print(time[r][c], end=' ')
    print()