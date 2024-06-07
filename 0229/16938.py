from itertools import combinations

N, L, R, X = map(int, input().split())
arr = list(map(int, input().split()))

# 15개밖에 안되니까 걍 조합으로 하면 안되나?
cnt = 0
for i in range(1, N + 1):
  com = combinations(arr, i)
  for nums in com:
    if L <= sum(nums) <= R and max(nums) - min(nums) >= X:
      cnt += 1
      
print(cnt)