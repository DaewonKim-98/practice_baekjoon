import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(i, depth):
    depths[i] = depth
    for j in link[i]:
        if visited[j] == 0:
            visited[j] = 1
            parents[j] = i
            dfs(j, depth + 1)

N = int(input().strip())
link = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().strip().split())
    link[a].append(b)
    link[b].append(a)

# dfs로 부모 리스트 저장
parents = [0] * (N + 1)
depths = [0] * (N + 1)
visited = [0] * (N + 1)
visited[1] = 1
dfs(1, 0)
    
M = int(input().strip())
for _ in range(M):
    a, b = map(int, input().strip().split())
    # rlvdl akwcnrh ckwrl ah hangle no shit
    while depths[a] > depths[b]:
        a = parents[a]
    while depths[a] < depths[b]:
        b = parents[b]
    
    while a != b:
        a = parents[a]
        b = parents[b]
    print(a)