import sys
import heapq

input = sys.stdin.readline
N = int(input().strip())
arr = []

for _ in range(N):
    x = int(input().strip())
    if x != 0:
        # 절댓값을 앞에 두고 x를 뒤에 두는 리스트를 힙에 푸쉬퓟퓟푸시퓌수푸쉬
        heapq.heappush(arr, [abs(x), x])
    else:
        if arr:
            delete = heapq.heappop(arr)
            print(delete[1])
        else:
            print(0)