from math import sqrt
from collections import deque

# 1000부터 9999까지의 소수
sosu_list = []
for i in range(1000, 10000):
  isSosu = True
  for j in range(2, int(sqrt(i)) + 1):
    if i % j == 0:
      isSosu = False
      break
  
  if isSosu == True:
    sosu_list.append(str(i))
    

def bfs(a):
  visited.add(a)
  q = deque()
  q.append((a, 0))
  
  while q:
    a, cnt = q.popleft()
    # b와 같게 된다면
    if a == b:
      print(cnt)
      return
      
    # 아니면 소수를 돌면서 하나가 다른 것이 나올 때까지
    for sosu in sosu_list:
      if sosu not in visited:
        for i in range(4):
          # 하나가 다른 것이 나온다면
          if a[0:i] + a[i + 1:4] == sosu[0:i] + sosu[i + 1:4]:
            visited.add(sosu)
            q.append((sosu, cnt + 1))
  
  # 다 돌아도 없으면
  print('Impossible')
  return

T = int(input())

for case in range(1, T + 1):
  a, b = map(str, input().split())
  
  # 1000부터 9999까지 모든 소수 찾은 다음에 bfs를 통해 하면 될듯
  visited = set()
  bfs(a)