import sys
input = sys.stdin.readline

M, N, L = map(int, input().strip().split())
gun = list(map(int, input().strip().split()))
animal = [tuple(map(int, input().strip().split())) for _ in range(N)]

gun.sort()
animal.sort()
cnt = 0

# 이분탐색으로 걍 해야하나 어케하지ㅜ미낭루ㅏㅣ먼ㅇ후마ㅣ널머ㅏㄴㅇㄻ나ㅣ후
for i in range(N):
  start = 0
  end = M - 1
  while start <= end:
    middle = (start + end) // 2
    if abs(gun[middle] - animal[i][0]) + animal[i][1] <= L:
      cnt += 1
      break
    if gun[middle] <= animal[i][0]:
      start = middle + 1
    else:
      end = middle - 1
      
print(cnt)