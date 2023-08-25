import sys
input = sys.stdin.readline

N = int(input().strip())
arr = [list(map(int, input().split())) for _ in range(N)]
# 각 기둥의 위치에 따라 오름차순으로 정렬
arr.sort(key=lambda x : x[0])
# 높이의 최댓값 인덱스의 최소부터 최대 구하기
max_idx1 = 0
max_idx2 = 0
for i in range(N):
    if arr[max_idx1][1] < arr[i][1]:
        max_idx1 = i
    if arr[max_idx2][1] <= arr[i][1]:
        max_idx2 = i
# 높이가 최대일 때까지 높은 것이 나오면 그 인덱스에서 최대 높이까지만큼 밑변으로
# 하는 직사각형의 넓이
higher = 0
area = 0
for i in range(max_idx1 + 1):
    if arr[higher][1] < arr[i][1]:
        # 넓이와 높은 높이를 가진 인덱스 갱신
        area += (arr[i][0] - arr[higher][0]) * arr[higher][1]
        higher = i

# 최대 높이 부분의 넓이
area += (arr[max_idx2][0] + 1 - arr[max_idx1][0]) * arr[max_idx1][1]   
# 최대 높이 이후의 넓이, 뒤에서부터 보면 편하다
higher = N - 1
for i in range(N - 1, max_idx2 - 1, -1):
    if arr[higher][1] < arr[i][1]:
        # 넓이와 높은 높이를 가진 인덱스 갱신
        area += (arr[higher][0] - arr[i][0]) * arr[higher][1]
        higher = i

print(area)
