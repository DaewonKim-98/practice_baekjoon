import sys
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
  N, M, K = map(int, input().strip().split())
  arr = list(map(int, input().strip().split()))
  # 처음 집과 마지막 집 연결
  arr += arr[0:M - 1]
  arr = [0] + arr
  # 누적합
  for i in range(1, len(arr)):
    arr[i] += arr[i - 1]
  # print(arr)
  cnt = 0
  if N == M:
    if arr[1 + M - 1] - arr[0] < K:
      cnt += 1
  else:
    for i in range(1, N + 1):
      if arr[i + M - 1] - arr[i - 1] < K:
        cnt += 1
  print(cnt)