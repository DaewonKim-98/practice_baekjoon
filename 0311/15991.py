T = int(input())

# 그냥 모든 경우의 수
arr = [0] * (100000 + 1)
arr[1] = 1
arr[2] = 2
arr[3] = 4

for i in range(4, 100001):
  arr[i] = (arr[i - 1] + arr[i - 2] + arr[i - 3]) % 1000000009

dp = [0] * (100000 + 1)
dp[1] = 1
dp[2] = 2
dp[3] = 2

# dp[i]는 i가 홀수일 때는 가운데 1, 3 짝수일 때는 가운데 2, x
# 모든 경우의 수로 생각해서 좌우 만들어야함
for i in range(4, 100001):
  if i % 2 == 0:
    dp[i] = (arr[i // 2] + arr[i // 2 - 1]) % 1000000009
  else:
    dp[i] = (arr[i // 2] + arr[i // 2 - 1]) % 1000000009
  

for case in range(1, T + 1):
  N = int(input())
  print(dp[N])