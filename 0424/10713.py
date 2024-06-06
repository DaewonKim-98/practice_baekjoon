import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
prices = [0] + [list(map(int, input().strip().split())) for _ in range(N - 1)]

# 각 열차를 얼마나 타는지 확인
# 각 열차의 처음은 + 마지막은 -
train = [0] * (N + 1)
for i in range(M - 1):
  if arr[i] < arr[i + 1]:
    train[arr[i]] += 1
    train[arr[i + 1]] -= 1
  else:
    train[arr[i + 1]] += 1
    train[arr[i]] -= 1
    
# 이걸 누적합으로 만들면 각 열차에 대해 얼마나 타는지 구할 수 있음
for i in range(N):
  train[i + 1] += train[i]
  
# 이제 비용을 생각해서 ic카드를 사는게 싸면 그거, 아니면 티켓
minPrice = 0
for i in range(1, N):
  minPrice += min(train[i] * prices[i][0], prices[i][2] + train[i] * prices[i][1])

print(minPrice)