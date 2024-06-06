import sys
input = sys.stdin.readline

while True:
  N, K = map(int, input().strip().split())
  if N == 0 and K == 0:
    break
  arr = list(map(int, input().strip().split()))
  if K == arr[0]:
    print(0)
    continue
  parents = [0]
  cnt = 0
  cousinCnt = 0
  kSibling = 0
  kCousin = 0
  findK = False
  firstFindK = False
  findKCousin = False
  lastCnt = False
  while True:
    for i in parents:
      # 부모가 형제가 아니면 사촌이 아니므로
      if arr[i] != arr[i - 1] + 1:
        cousinCnt = 0
        findKCousin = False
      sibling = 0
      while True:
        if parents[-1] + 1 + cnt == N - 1:
          # K를 찾으면
          if arr[parents[-1] + 1 + cnt] == K:
            findK = True
            firstFindK = True
            findKCousin = True
          sibling += 1
          cnt += 1
          cousinCnt += 1
          lastCnt = True
          break
        # 형제면
        if arr[parents[-1] + 1 + cnt] + 1 == arr[parents[-1] + 1 + cnt + 1]:
          # K를 찾으면
          if arr[parents[-1] + 1 + cnt] == K:
            findK = True
            firstFindK = True
            findKCousin = True
          sibling += 1
          cnt += 1
          cousinCnt += 1
        # 마지막 형제도 세줘야 하므로
        else:
          # K를 찾으면
          if arr[parents[-1] + 1 + cnt] == K:
            findK = True
            firstFindK = True
            findKCousin = True
          sibling += 1
          cnt += 1
          cousinCnt += 1
          break
      if findK == True and firstFindK == True:
        kSibling = sibling
        firstFindK = False
      if findK == True and findKCousin == True:
        kCousin = cousinCnt
      if lastCnt == True:
        break
    if findK == True:
      break
    parentsCopy = parents.copy()
    parents = []
    for i in range(parentsCopy[-1] + 1, parentsCopy[-1] + 1 + cnt):
      parents.append(i)
    cnt = 0
    # print(parents)
      
  # 사촌의 수는 전체 에서 형제만 뺀 것
  # print(kCousin)
  # print(kSibling)
  print(kCousin - kSibling)