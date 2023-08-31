import sys
input = sys.stdin.readline

N = int(input().strip())

# N까지의 제곱 수들의 리스트
arr = []
for i in range(250):
    if i ** 2 <= N:
        arr.append(i ** 2)

sum_arr = []
for i in arr:
    for j in arr:
        sum_arr.append(i + j)

result = 0
# 제곱 수들 1개의 합
if N in arr:
    print(1)
    exit()

# 제곱 수들 2개의 합
for i in arr:
    for j in arr:
        if i + j == N:
            print(2)
            exit()

# 제곱 수들 3개의 합
for i in arr:
    for j in sum_arr:
        if i + j == N:
            print(3)
            exit()

print(4)
