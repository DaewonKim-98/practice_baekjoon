import sys
input = sys.stdin.readline

N = int(input().strip())
if N == 0:
  print(0)
  exit()
arr = []
for _ in range(N):
  p, d = map(int, input().strip().split())
  arr.append((d, p))
arr.sort(reverse=True)  

# 늦게 하는 강연부터 높은거 담기
lecture = [0] * 10001
confirmed = set()

for i in range(10000, -1, -1):
  maxMoney = 0
  lectureDay = 0
  for j in range(N):
    # 강의 날짜에 맞으면
    if i <= arr[j][0]:
      # 확정된 강의가 아니면
      if j not in confirmed:
        # print(i, arr[j], maxMoney)
        # 최대 찾기
        if maxMoney < arr[j][1]:
          maxMoney = arr[j][1]
          lectureDay = j
  lecture[i] = maxMoney
  confirmed.add(lectureDay)
lecture[arr[0][0]] = arr[0][1]

# 0일 빼기
lecture.pop(0)    
print(sum(lecture))