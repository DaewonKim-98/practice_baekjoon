import sys
input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())
x = list(map(int, input().split()))

# 굴다리 사이 거리의 반
arr = []
for i in range(M - 1):
    if (x[i + 1] - x[i]) % 2 == 1:
        arr.append((x[i + 1] - x[i]) // 2 + 1)
    
    else:
        arr.append((x[i + 1] - x[i]) // 2)

# 처음와 끝에서 가로등까지의 거리
arr.append(x[0])
arr.append(N - x[-1])
# 굴다리 사이의 거리들과 처음과 끝 중에서 최댓값
print(max(arr))