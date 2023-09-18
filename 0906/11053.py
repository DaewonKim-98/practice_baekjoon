import sys
input = sys.stdin.readline

A = int(input().strip())
arr = list(map(int, input().split()))

part_arr = [1] * A
for i in range(A):
    # 자신 이전에 최대 수가 있고 자신과 비교해서 수열의 개수가 작으면 수열 개수 추가
    for j in range(i):
        if arr[j] < arr[i]:
            part_arr[i] = max(part_arr[i], part_arr[j] + 1)
            
print(max(part_arr))