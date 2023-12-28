# 저 정도로 머리가 출중하면 이딴 게임의 심판 같은걸 할까?
import sys

def make_tree(start, end, i):
    if start == end:
        segment_tree[i] = arr[start]
        return segment_tree[i]
    
    mid = (start + end) // 2
    segment_tree[i] = make_tree(start, mid, i * 2) + make_tree(mid + 1, end, i * 2 + 1)
    return segment_tree[i]

def find(start, end, i, x, y):
    if end < x or y < start:
        return 0
    
    elif x <= start and end <= y:
        return segment_tree[i]
    
    mid = (start + end) // 2
    return find(start, mid, i * 2, x, y) + find(mid + 1, end, i * 2 + 1, x, y)

def update(start, end, i, a, b):
    if end < a or a < start:
        return
    
    elif start == end:
        segment_tree[i] = b
        return
        
    mid = (start + end) // 2
    update(start, mid, i * 2, a, b)
    update(mid + 1, end, i * 2 + 1, a, b)
    segment_tree[i] = segment_tree[i * 2] + segment_tree[i * 2 + 1]
    return

input = sys.stdin.readline
N, Q = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))

segment_tree = [0] * (N * 4)

make_tree(0, N - 1, 1)

for _ in range(Q):
    x, y, a, b = map(int, input().strip().split())
    # print(segment_tree)
    if x <= y:
        print(find(0, N - 1, 1, x - 1, y - 1))
    elif x > y:
        print(find(0, N - 1, 1, y - 1, x - 1))
        
    update(0, N - 1, 1, a - 1, b)
    arr[a - 1] = b
    # print(segment_tree)
    