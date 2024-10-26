import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
arr = [int(input().strip()) for _ in range(N)]

# 이분탐색 해야할 듯
start = 1
end = 1000000000

while start <= end:
  mid = (start + end) // 2

  cnt = 1
  k = mid
  for money in arr:
    # 인출해서도 사용하지 못하면
    if mid < money:
      cnt = M + 1
      break
    # k로 사용할 수 있으면
    if money <= k:
      k -= money
    # k로 사용하지 못하면 인출하고 사용
    else:
      k = mid
      cnt += 1
      k -= money
  # 인출 횟수가 M보다 작으면 인출할 수 있는 금액을 줄여야 하므로
  if cnt <= M:
    end = mid - 1
  else:
    start = mid + 1

print(start)