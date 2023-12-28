import sys
input = sys.stdin.readline

def segment_tree(start, end, i):
    if start == end:
        tree[i] = [arr[start], arr[end]]
        return tree[i]

    mid = (start + end) // 2
    left, right = segment_tree(start, mid, i * 2), segment_tree(mid + 1, end, i * 2 + 1)
    tree[i] = [min(left[0], right[0]), max(left[1], right[1])]
    return tree[i]

def find(start, end, i, left, right):
    if end < left or start > right:
        return [1000000000, 1]
    if left <= start and right >= end:
        return tree[i]
    mid = (start + end) // 2
    l, r = find(start, mid, i * 2, left, right), find(mid + 1, end, i * 2 + 1, left, right)
    return [min(l[0], r[0]), max(l[1], r[1])]

N, M = map(int, input().strip().split())
arr = [int(input().strip()) for _ in range(N)]
tree = [[1000000000, 1] for _ in range(N * 4)]

segment_tree(0, N - 1, 1)

for _ in range(M):
    a, b = map(int, input().strip().split())
    a -= 1
    b -= 1
    small, big = find(0, N - 1, 1, a, b)
    print(small, end=' ')
    print(big)