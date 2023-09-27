arr = [list(map(int, input().split())) for _ in range(5)]

# 방향
dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

# 이동하면서 수를 만들 함수
def makenum(r, c, cnt, num):
  global num_count
  num += str(arr[r][c])
  if cnt == 5:
    if num not in num_set:
      num_set.add(num)
      num_count += 1
    return
  for d in dir:
    nr, nc = r + d[0], c + d[1]
    if 0 <= nr < 5 and 0 <= nc < 5:
      makenum(nr, nc, cnt + 1, num)


# 배열을 돌면서 서로 다른 여섯자리의 수들 set에 추가
num_count = 0
num_set = set()
for r in range(5):
  for c in range(5):
    cnt = 0
    num = ''
    makenum(r, c, cnt, num)
    
print(num_count)