N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()

# 망할 시간초과 ㅡㅡ 밑에 보니까 이분탐색이니까 이분 탐색으로 풀어보즈아!!
# 이분 탐색 절대 안되는데 어케하는거지
# 두개의 합이랑 최댓값이랑 차이 생각하면 이중포문 2개로 되나?
# 안되면 진짜 아오 어케하는거지 일단 해봄

sum_set = set()

for i in arr:
    for j in arr:
        sum_set.add(i + j)

# print(sum_set)
# 최댓값부터 내려오면서 z값 찾기
result = 0
for k in range(N - 1, -1, -1):
    for j in range(k - 1, -1, -1):
        if arr[k] - arr[j] in sum_set:
            result = arr[k]
            print(result)
            exit()

