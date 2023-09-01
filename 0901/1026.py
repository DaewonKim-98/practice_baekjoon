import sys
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A에서 가장 큰 값들과 B에서 작은 값들을 곱해서 플러스
s = 0
A.sort()
B.sort(reverse=True)
for i in range(N):
    s += A[i] * B[i]

print(s)