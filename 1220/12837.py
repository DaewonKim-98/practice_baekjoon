import sys
input = sys.stdin.readline

def change(start, end, i):
    if end < b - 1 or b - 1 < start:
        return
    
    if start == end:
        segment_tree[i] = c
        return
    
    mid = (start + end) // 2
    change(start, mid, i * 2)
    change(mid + 1, end, i * 2 + 1)
    segment_tree[i] = segment_tree[i * 2] + segment_tree[i * 2 + 1]
    return

def find(start, end, i, b, c):
    if end < b or c < start:
        return 0
    
    if b <= start and end <= c:
        return segment_tree[i]

    mid = (start + end) // 2
    return find(start, mid, i * 2, b, c) + find(mid + 1, end, i * 2 + 1, b, c)

# 누적합이네
N, Q = map(int, input().strip().split())
arr = [0] * N

segment_tree = [0] * (N * 4)

for _ in range(Q):
    a, b, c = map(int, input().strip().split())
    if a == 1:
        c += arr[b - 1]
        change(0, N - 1, 1)
        arr[b - 1] = c
    
    else:
        print(find(0, N - 1, 1, b - 1, c - 1))