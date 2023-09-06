import sys
input = sys.stdin.readline

A = int(input().strip())
arr = list(map(int, input().split()))

for i in range(A):
    part_arr = [1] * A
    k = i
    # 자기보다 큰게 그 뒤에 생기면 1씩 추가해서 가장 많은 카운트를 가진 것이 가장 많은 증가 부분 수열 개수
    for j in range(i, A):
        # 자신보다 더 큰 것이 있으면 새로 자신을 갱신하고 카운트
        if arr[k] < arr[j]:
            k = j
            part_arr[i] += 1
print(part_arr)
print(max(part_arr))