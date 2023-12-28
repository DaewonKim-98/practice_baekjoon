import sys
import heapq
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

def dfs(i):
    global total_money
    # 넘어가면 돈이 부족하므로 끝
    if total_money > K:
        print('Oh no')
        exit()
        
    for j in link[i]:
        if visited[j] == 0:
            visited[j] = 1
            dfs(j)
            

# dfs
N, M, K = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))

link = [set() for _ in range(N)]
for _ in range(M):
    v, w = map(int, input().strip().split())
    link[v - 1].add(w - 1)
    link[w - 1].add(v - 1)

heap = []
visited = [0] * N
for i in range(N):
    heapq.heappush(heap, (arr[i], i))
    
total_money = 0
# 모두 방문할 때까지 while문 반복
while sum(visited) < N:
    money, friend = heapq.heappop(heap)
    # 방문하지 않았으면
    if visited[friend] == 0:
        total_money += money
        visited[friend] = 1
        # 연결된 친구들 모두 찾기
        dfs(friend)
        
print(total_money)