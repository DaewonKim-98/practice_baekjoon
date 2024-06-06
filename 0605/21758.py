N = int(input())
arr = list(map(int, input().split()))
allHoney = sum(arr)

# 왼쪽에서 오른쪽 누적합 - 벌통이 오른쪽에 있을 때
sumArr = arr.copy()
for i in range(1, N):
  sumArr[i] = sumArr[i - 1] + sumArr[i]
  
maxHoney = 0
for i in range(1, N):
  maxHoney = max(maxHoney, allHoney - arr[0] - arr[i] + sumArr[N - 1] - sumArr[i - 1] - arr[i])
  
# 오른쪽에서 왼쪽 누적합 - 벌통이 왼쪽에 있을 때
sumArr = arr.copy()
for i in range(N - 2, -1, -1):
  sumArr[i] = sumArr[i + 1] + sumArr[i]
  
for i in range(N - 2, -1, -1):
  maxHoney = max(maxHoney, allHoney - arr[N - 1] - arr[i] + sumArr[0] - sumArr[i + 1] - arr[i])

# 벌통이 가운데에 있을 때에는 가장 큰 값에 있어야 하므로
maxHoney = max(maxHoney, allHoney - arr[0] - arr[N - 1] + max(arr))

print(maxHoney)