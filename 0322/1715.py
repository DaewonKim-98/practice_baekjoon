import heapq

N = int(input())
arr = [int(input()) for _ in range(N)]
heapq.heapify(arr)

# 작은 것들끼리 계속 더하면 될듯?
sums = 0
while len(arr) > 1:
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    heapq.heappush(arr, a + b)
    sums += a + b
    
print(sums)