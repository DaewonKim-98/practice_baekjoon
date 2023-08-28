N = int(input())

arr = []
for i in range(N):
    arr.append(int(input()))

# 최댓값의 인덱스
max_idx = 0
for i in range(N):
    if arr[max_idx] <= arr[i]:
        max_idx = i

# 매수해야 하는 사람의 최솟값
cnt = 0

# 최댓값의 인덱스가 0일 때까지 반복
while max_idx != 0:
    # 최댓값에서 1 마이너스, 0에서 1 플러스
    arr[max_idx] -= 1
    arr[0] += 1
    # 다시 최댓값 인덱스 갱신
    for i in range(N):
        if arr[max_idx] <= arr[i]:
            max_idx = i
    cnt += 1

print(cnt)
