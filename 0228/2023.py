from math import sqrt
from collections import deque

# 각 수마다 따로 하기 메모리초광ㅁ닒ㄴ어ㅏㅎㅁㄴ';ㄹ
def findSosu(num):
  # 그냥 다시?
  for i in range(2, int(sqrt(num)) + 1):
    if num % i == 0:
      return False
  return True

def bfs(i):
  q = deque()
  q.append((i, 1))
  
  # 되면 소수 추가
  while q:
    num, zari = q.popleft()
    # 자리가 N자리가 된다면
    if zari == N:
      print(num)
      continue
    
    for i in range(1, 10):
      if findSosu(int(str(num) + str(i))) == True:
        q.append((int(str(num) + str(i)), zari + 1))

N = int(input())
# 소수 찾는 시간 줄여야함
sosuList = [0] + [0] + [1] * (N - 1)

# dfs를 통해 N자리 소수 찾기 - 메모리초과남 ㅁㄴ아ㅣㄻ나ㅣ bfs를 통해서?
for i in [2, 3, 5, 7]:
  bfs(i)