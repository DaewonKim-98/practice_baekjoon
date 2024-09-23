import sys
import heapq
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
  queueP = []
  queueM = []
  allQueue = []
  qDic = {}
  heapq.heapify(queueP)
  heapq.heapify(queueM)
  K = int(input().strip())
  for _ in range(K):
    a, b = map(str, input().strip().split())
    # +와-로 넣어 최대 또는 최소 삭제 가능하게
    if a == 'I':
      heapq.heappush(queueP, int(b))
      heapq.heappush(queueM, -int(b))
      allQueue.append(int(b))
      if int(b) in qDic:
        qDic[int(b)] += 1
      else:
        qDic[int(b)] = 1
    else:
      if allQueue:
        if b == '1':
          while True:
            maxV = queueM[0]
            if qDic[-maxV] == 0:
              while queueM and maxV == queueM[0]:
                heapq.heappop(queueM)
            else:
              cnt = 0
              while queueM and maxV == queueM[0]:
                cnt += 1
                heapq.heappop(queueM)
              for _ in range(qDic[-maxV] - 1):
                heapq.heappush(queueM, maxV)
              qDic[-maxV] -= 1
              break
        else:
          while True:
            minV = queueP[0]
            if qDic[minV] == 0:
              while queueP and minV == queueP[0]:
                heapq.heappop(queueP)
            else:
              cnt = 0
              while queueP and minV == queueP[0]:
                cnt += 1
                heapq.heappop(queueP)
              for _ in range(qDic[minV] - 1):
                heapq.heappush(queueP, minV)
              qDic[minV] -= 1
              break

        allQueue.pop()
      if not allQueue:
        queueM = []
        queueP = []

  # 전부 다 삭제했으면
  while queueM and qDic[-queueM[0]] == 0:
      heapq.heappop(queueM)
  while queueP and qDic[queueP[0]] == 0:
      heapq.heappop(queueP)
  if not allQueue:
    print('EMPTY')
  else:
    print(-heapq.heappop(queueM), heapq.heappop(queueP))