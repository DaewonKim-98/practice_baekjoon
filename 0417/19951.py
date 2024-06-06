import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))

# 각 칸의 처음과 끝에 저장
lst = [0] * (N + 1)
for _ in range(M):
  a, b, k = map(int, input().strip().split())
  # a를 그냥 넣고 나중에 a부터 쭉 더하는데 b가 지나면 다시 빼주면 되나?
  lst[a - 1] += k
  lst[b] -= k
  
# 얘를 누적합을 하면 처음 a부터 쭉 더해지고 b이후에는 다시 빼지게 되니까 오
# 이후에는 안더해지게 되는 오 마법 오
for i in range(1, N + 1):
  lst[i] += lst[i - 1]
  
narr = [0] * N
for i in range(N):
  narr[i] = arr[i] + lst[i]
  
for i in range(N):
  print(narr[i], end=' ')
