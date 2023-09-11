N, X = map(int, input().split())
arr = [0] + list(map(int, input().split()))

lst = [0] * (N + 1)
for i in range(1, X + 1):
    # 합 리스트에 X만큼 일단 추가
    lst[i] = arr[i] + lst[i - 1]

# X일까지의 합을 lst에 넣기
for j in range(X + 1, N + 1):
    lst[j] = lst[j - 1] - arr[j - X] + arr[j]

# 합 중에서 최댓값과 그 갯수 출력\
if max(lst) == 0:
    print('SAD')

else:
    print(max(lst))
    print(lst.count(max(lst)))