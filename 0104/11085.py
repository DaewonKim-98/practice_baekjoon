import heapq

def find_road(c):
    visited = [0] * p
    heap = []
    heapq.heappush(heap, [0, c])
    
    while heap:
        # print(heap)
        width, w = heapq.heappop(heap)
        # 도착하면
        if visited[w] == 0:
            visited[w] = width
            if w == v:
                max_value = -1000
                for i in range(p):
                    if visited[i] != 0 and max_value < visited[i]:
                        max_value = visited[i]
                return max_value
            for lst in arr[w]:
                heapq.heappush(heap, [lst[0], lst[1]])

p, w = map(int, input().split())
c, v = map(int, input().split())

arr = [[] for _ in range(p)]
for _ in range(w):
    s, e, width = map(int, input().split())
    arr[s].append([-width, e])
    arr[e].append([-width, s])
# print(arr)
# 다이스트라
print(-find_road(c))