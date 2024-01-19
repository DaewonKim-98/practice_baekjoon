from copy import deepcopy
from collections import deque

dir = [[0, 1], [1, 0], [-1, 0], [0, -1]]

# 주위에 인접한 핀이 있는 것 판단
def link_pin(r, c, arr):
  for d in dir:
    nr, nc = r + d[0], c + d[1]
    if 0 <= nr < 5 and 0 <= nc < 9:
      # 인접한 핀이 있으면 True 반환
      if arr[nr][nc] == 'o':
        return True
  return False
  

# 각 r, c에 대해 실행
def game(r, c, arr):
  global min_move
  global min_pin
  
  q = deque()
  q.append((r, c, arr, 0))
  m = 0
  
  while q:
    r, c, arr, move = q.popleft()
    m = move
    carr = deepcopy(arr)
    print(carr)
    
    # 전체를 돌았어도 움직일 수 있는 핀이 없으면
    not_link = True
    for a in range(5):
      for b in range(9):
        if carr[a][b] == 'o' and link_pin(a, b, carr):
          not_link = False
          
    if not_link == True:
      # 갱신
      pin = 0
      for r in range(5):
        for c in range(9):
          if arr[r][c] == 'o':
            pin += 1
            
      if min_pin > pin:
        min_pin = min(min_pin, pin)
        min_move = min(min_move, m)
      return
    
    # 핀 움직이기
    for d in dir:
      nr, nc = r + d[0], c + d[1]
      if 0 <= nr < 5 and 0 <= nc < 9 and 0 <= r + d[0] * 2 < 5 and 0 <= c + d[1] * 2 < 9:
        # 인접한 핀이 있고 그 다음이 공백이면
        if carr[nr][nc] == 'o' and carr[r + d[0] * 2][c + d[1] * 2] == '.':
          # 공백으로 바꾸고 핀 옮기기
          carr[r][c] = '.'
          carr[nr][nc] = '.'
          carr[r + d[0] * 2][c + d[1] * 2] = 'o'
    
    # 다시 전체를 돌고 움직일 수 있는 핀이 있으면 q에 추가
    for a in range(5):
      for b in range(9):
        if carr[a][b] == 'o' and link_pin(a, b, carr):
          q.append((a, b, carr, move + 1))
          

T = int(input())


for case in range(T):
  arr = [list(input()) for _ in range(5)]
  if case != T - 1:
    input()
  
  # 2개가 같이 있을 때 넘였을 때 빈 공간이고 인접한 부분에 o가 있는 곳으로
  # 최대한 가게끔 만들기 모든 o를 다 탐색해서 최솟값 찾기
  min_pin = 8
  min_move = 100
  for r in range(5):
    for c in range(9):
      if arr[r][c] == 'o':
        game(r, c, arr)
        
  print(min_pin, min_move)
  