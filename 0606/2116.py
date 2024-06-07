import sys
input = sys.stdin.readline

def calculate(up, sum):
  for i in range(1, N):
    if arr[i].index(up) == 0:
      up = arr[i][5]
      sum += max(arr[i][1:5])
    elif arr[i].index(up) == 5:
      up = arr[i][0]
      sum += max(arr[i][1:5])
    elif arr[i].index(up) == 1:
      up = arr[i][3]
      sum += max(arr[i][0], arr[i][2], arr[i][4], arr[i][5])
    elif arr[i].index(up) == 3:
      up = arr[i][1]
      sum += max(arr[i][0], arr[i][2], arr[i][4], arr[i][5])
    elif arr[i].index(up) == 2:
      up = arr[i][4]
      sum += max(arr[i][0], arr[i][1], arr[i][3], arr[i][5])
    elif arr[i].index(up) == 4:
      up = arr[i][2]
      sum += max(arr[i][0], arr[i][1], arr[i][3], arr[i][5])
  return sum
  

N = int(input().strip())
arr = [list(map(int, input().strip().split())) for _ in range(N)]

# 1번 주사위를 놓는거에 따라서 나머지가 걍 다 바뀌므로 1번 주사위 ABC로 찾기
# A가 위로 갈 때
aSum = max(arr[0][1:5])
up = arr[0][0]
aSum = calculate(up, aSum)

# B가 위로 갈때
bSum = max(arr[0][0], arr[0][2], arr[0][4], arr[0][5])
up = arr[0][1]
bSum = calculate(up, bSum)

# C가 위로 갈때
cSum = max(arr[0][0], arr[0][1], arr[0][3], arr[0][5])
up = arr[0][2]
cSum = calculate(up, cSum)

# D가 위로 갈 때
dSum = max(arr[0][0], arr[0][2], arr[0][4], arr[0][5])
up = arr[0][3]
dSum = calculate(up, dSum)

# E가 위로 갈때
eSum = max(arr[0][0], arr[0][1], arr[0][3], arr[0][5])
up = arr[0][4]
eSum = calculate(up, eSum)

# F가 위로 갈때
fSum = max(arr[0][1:5])
up = arr[0][5]
fSum = calculate(up, fSum)
  
print(max(aSum, bSum, cSum, dSum, eSum, fSum))