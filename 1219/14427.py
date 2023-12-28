import sys
from copy import deepcopy
input = sys.stdin.readline

def make_tree(start, end, i):
    if start == end:
        segment_tree[i] = [arr[start], start]
        return segment_tree[i]

    mid = (start + end) // 2
    left, right = make_tree(start, mid, i * 2), make_tree(mid + 1, end, i * 2 + 1)
    if left[0] <= right[0]:
        segment_tree[i] = left
    else:
        segment_tree[i] = right
        
    return segment_tree[i]

def update(start, end, i):
    if end < lst[1] - 1 or lst[1] - 1 < start:
        return
    
    if start == end:
        segment_tree[i] = [lst[2], start]
        return
    
    mid = (start + end) // 2
    update(start, mid, i * 2)
    update(mid + 1, end, i * 2 + 1)
    
    left, right = segment_tree[i * 2], segment_tree[i * 2 + 1]
    # print(left, right)
    if left[0] <= right[0]:
        segment_tree[i] = left
    else:
        segment_tree[i] = right
    return

N = int(input().strip())
arr = list(map(int, input().strip().split()))

segment_tree = [[1000000001, 100001] for _ in range(N * 4)]

make_tree(0, N - 1, 1)
# print(segment_tree)
M = int(input().strip())
for _ in range(M):
    lst = list(map(int, input().strip().split()))
    if lst[0] == 1:
        update(0, N - 1, 1)
        arr[lst[1] - 1] = lst[2]
        
    else:
        print(segment_tree[1][1] + 1)