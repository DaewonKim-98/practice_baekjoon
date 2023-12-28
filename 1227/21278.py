from collections import deque

# bfs를 통해 시간 찾기
def bfs(k):
    global time
    visited = [0] * (N + 1)
    q = deque()
    visited[k] = 1
    q.append(k)
    
    while q:
        building = q.popleft()
        # building이 i 나 j에 도착한다면
        if building == i or building == j:
            time += (visited[building] - 1) * 2
            return
        
        # 연결된 간선
        for l in link[building]:
            # print(l)
            if visited[l] == 0:
                q.append(l)
                visited[l] = visited[building] + 1

N, M = map(int, input().split())
link = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    link[a].append(b)
    link[b].append(a)

# print(link)
min_time = 20000
building1 = 0
building2 = 0
# 두 건물
for i in range(N, 1, -1):
    for j in range(i - 1, 0, -1):
        # 다른 모든 건물에서 이 두 건물까지의 최소 왕복 시간의 합
        time = 0
        for k in range(1, N + 1):
            if k != i and k != j:
                bfs(k)
        
        # 다 돌았으면 time비교
        if min_time >= time:
            # 갱신
            min_time = time
            building1 = j
            building2 = i
            
print(building1, end=' ')
print(building2, end=' ')
print(min_time)