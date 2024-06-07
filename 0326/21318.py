import sys
input = sys.stdin.readline

N = int(input().strip())
arr = [0] + list(map(int, input().strip().split()))
Q = int(input().strip())

# 실수, 성공하는 것 미리 찾아두기
mistake = [0] * (N + 1)
for i in range(1, N):
  if arr[i] > arr[i + 1]:
    mistake[i] = 1
    
# 실수 성공 누적합
sumMistake = [0] * (N + 1)
for i in range(1, N + 1):
  sumMistake[i] += mistake[i] + sumMistake[i - 1]
# print(mistake)
# print(sumMistake)

for _ in range(Q):
  x, y = map(int, input().strip().split())
  cnt = sumMistake[y - 1] - sumMistake[x - 1]
      
  print(cnt)
