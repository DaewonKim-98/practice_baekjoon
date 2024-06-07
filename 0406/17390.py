import sys
input = sys.stdin.readline

N, Q = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
arr.sort()

# 누적합
arrSum = arr.copy()
for i in range(1, N):
    arrSum[i] = arrSum[i - 1] + arrSum[i]
arrSum = [0] + arrSum
    
for _ in range(Q):
    L, R = map(int, input().strip().split())
    L -= 1
    R -= 1
    print(arrSum[R + 1] - arrSum[L])