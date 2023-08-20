import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))
# 결과가 없으면 result = -1
result = -1

def merge_sort(unsorted_list):
    # 크기가 1이하면 반환
    if len(unsorted_list) <= 1:
        return unsorted_list
 
    # 리스트를 2분할 
    mid = len(unsorted_list) // 2
    left = unsorted_list[:mid]
    right = unsorted_list[mid:]
    
    # 2분할한 리스트를 각각 merge sort진행
    left_ = merge_sort(left)
    right_ = merge_sort(right)
    return merge(left_, right_)

def merge(left, right):
    global cnt
    global result
    i, j = 0,0
    sorted_list = []
    
    while i < len(left) and j < len(right):
        cnt += 1
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
        # 저장 횟수가 K번 째이면 그 수를 출력
        if cnt == K:
            result = sorted_list[-1]

    while i < len(left):
        cnt += 1
        sorted_list.append(left[i])
        i += 1
        if cnt == K:
            result = sorted_list[-1]

    while j < len(right):
        cnt += 1
        sorted_list.append(right[j])
        j += 1
        if cnt == K:
            result = sorted_list[-1]

    return sorted_list

cnt = 0
merge_sort(arr)
print(result)
