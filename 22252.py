import sys
import heapq
input = sys.stdin.readline

Q = int(input().strip())
cnt = 0
gorillas = {}
for _ in range(Q):
  arr = list(map(str, input().strip().split()))
  if arr[0] == '1':
    if arr[1] in gorillas:
      for i in range(3, 3 + int(arr[2])):
        heapq.heappush(gorillas[arr[1]], -int(arr[i]))
    else:
      gorillas[arr[1]] = []
      for i in range(3, 3 + int(arr[2])):
        heapq.heappush(gorillas[arr[1]], -int(arr[i]))

  # 정보 사기
  else:
    # 정보의 수만큼
    if arr[1] in gorillas:
      for _ in range(min(len(gorillas[arr[1]]), int(arr[2]))):
        cnt += -heapq.heappop(gorillas[arr[1]])

print(cnt)