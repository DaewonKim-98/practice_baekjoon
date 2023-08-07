import sys

N = int(input())

arr = []
for i in range(N):
    arr += [int(sys.stdin.readline())]

# 뒤에서부터 큰 값들을 세야하므로 가장 뒤에 값을 max_stick으로 둔다.
max_stick = arr[-1]
cnt = 1
# 뒤에서부터 셀 때 큰 값이 나오면 cnt 1 추가 max 갱신
for j in range(N - 1, -1, -1):
    if arr[j] > max_stick:
        cnt += 1
        max_stick = arr[j]

print(cnt)