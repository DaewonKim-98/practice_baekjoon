import heapq

def bfs(i):
    global max_item
    visited = [0] * (N + 1)
    heap = []
    heapq.heappush(heap, (0, i))
    

    while heap:
        distance, area = heapq.heappop(heap)
        # 방문하지 않은 곳이고 거리가 M보다 작거나 같으면 갈 수 있으므로
        if visited[area] == 0 and distance <= M:
            visited[area] = 1

            for j in arr[area]:
                    heapq.heappush(heap, (j[0] + distance, j[1]))

    # 방문할 수 있는 곳을 모두 방문했으면
    item = 0
    # print(visited)
    for i in range(1, N + 1):
        if visited[i] != 0:
            item += items[i]

    if max_item < item:
        max_item = item


N, M, R = map(int, input().split())

# 각 구역의 아이템 수
items = [0] + list(map(int, input().split()))

# 간선 리스트
arr = [[] for _ in range(N + 1)]
for _ in range(R):
    a, b, l = map(int, input().split())
    arr[a].append((l, b))
    arr[b].append((l, a))

# 배열을 돌면서 bfs를 통해 최대 아이템 개수 찾기
max_item = 0
for i in range(1, N + 1):
    bfs(i)

print(max_item)