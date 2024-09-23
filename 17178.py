from collections import deque

N = int(input())
arr = []
for _ in range(N):
  people = list(map(str, input().split()))
  for person in people:
    arr.append(person)

# 티켓 순서로 정렬한 배열
sortedArr = sorted(arr, key=lambda x: [x[0], int(x[2:])])
sortedArr = deque(sortedArr)
# 대기실
waitingRoom = []

# 콘서트장에 입장시키면서 티켓 순서에 맞게 사람이 오면 공연장으로, 아니면 대기실로
for person in arr:
  # 입장 시키는 사람이 가장 빠른 사람이면
  if person == sortedArr[0]:
    sortedArr.popleft()
  else:
    # 대기실에 누가 있고 대기실에 가장 뒤의 사람이 가장 빠른 사람이면
    while waitingRoom and waitingRoom[-1] == sortedArr[0]:
      waitingRoom.pop()
      sortedArr.popleft()
    # 대기실에 갈 사람 대기실에 넣기
    waitingRoom.append(person)

# 나머지 대기실에 있는 사람들 입장시키기
for person in sortedArr:
  if person == waitingRoom[-1]:
    waitingRoom.pop()
  # 입장시킬 수 없으면 끝
  else:
    print('BAD')
    break
else:
  print('GOOD')