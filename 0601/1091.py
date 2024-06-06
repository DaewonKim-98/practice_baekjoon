N = int(input())
P = list(map(int, input().split()))
S = list(map(int, input().split()))
arr = [i for i in range(N)]

# 각 카드가 누구한테 가야하는지
dic = {
  0: set(),
  1: set(),
  2: set()
  }
for i in range(N):
  dic[P[i]].add(i)

# 카드를 섞고 이후에 카드가 잘 가는지 확인
copyArr = arr.copy()
cnt = 0
while True:
  # 섞은 카드를 돌면서 플레이어에게 잘 가는지 확인
  canGive = True
  for i in range(N):
    if copyArr[i] not in dic[i % 3]:
      canGive = False
      break
  # 잘 갔으면 끝
  if canGive == True:
    print(cnt)
    exit()
  cnt += 1
  mix = [0] * N
  # 카드 섞기
  for i in range(N):
    mix[S[i]] = copyArr[i]
  copyArr = mix.copy()
  
  # 다 섞은 카드가 다시 원래로 돌아갔으면 카드를 해당하는 플레이어에게 줄 수 없으므로
  if copyArr == arr:
    print(-1)
    exit()