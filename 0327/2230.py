import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
arr = [int(input().strip()) for _ in range(N)]
arr.sort()

# 투 포인트?
minSub = 2000000001
start = 0
end = 0
while end < N and start < N:
  if M <= arr[end] - arr[start] < minSub:
    minSub = arr[end] - arr[start]
    
  if M <= arr[end] - arr[start]:
    start += 1
    continue
  else:
    end += 1
    continue
  
print(minSub)