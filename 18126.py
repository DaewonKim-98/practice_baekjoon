import sys
sys.setrecursionlimit(100000)

def findDis(i, dis):
    global maxDis
    maxDis = max(maxDis, dis)
    
    for j in link[i]:
        if visited[j[0]] == 0:
            visited[j[0]] = 1
            findDis(j[0], dis + j[1])
            visited[j[0]] = 0

N = int(input())
link = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    link[a].append((b, c))
    link[b].append((a, c))

# 가장 먼 거리 구하기
maxDis = 0
visited = [0] * (N + 1)
visited[1] = 1
findDis(1, 0)
print(maxDis)