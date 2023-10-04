import heapq

n, m = map(int, input().split())
heap = list(map(int, input().split()))
heap.sort()

# 최소힙을 이용해 가장 낮은 점수 구하기
# i가 m이 될 때까지 반복
i = 0
while i < m:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    a, b = a + b, a + b
    heapq.heappush(heap, a)
    heapq.heappush(heap, b)
    i += 1

print(sum(heap))
