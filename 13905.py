import sys
import heapq
input = sys.stdin.readline

def goHyebeen(s, e):
    q = []
    visited = [0] * (N + 1)
    heapq.heapify(q)
    heapq.heappush(q, (-10000000, s))
    maxWeight = 0
    
    while q:
        weight, house = heapq.heappop(q)
        if house == e:
            maxWeight = max(maxWeight, -weight)
            continue
        if visited[house] == 0:
            visited[house] = 1
            for i in link[house]:
                heapq.heappush(q, (max(weight, -i[1]), i[0]))
            
    print(maxWeight)
    
N, M = map(int, input().strip().split())
s, e = map(int, input().strip().split())

link = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().strip().split())
    link[a].append((b, c))
    link[b].append((a, c))
    
# 가장 무겁게 ㄱㄱ
goHyebeen(s, e)