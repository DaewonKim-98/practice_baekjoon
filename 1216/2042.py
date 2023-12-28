import sys
input = sys.stdin.readline

def segment_tree(start, end, i):
    if start == end:
        tree[i] = arr[start]
        return tree[i]

    mid = (start + end) // 2
    left, right = segment_tree(start, mid, i * 2), segment_tree(mid + 1, end, i * 2 + 1)
    tree[i] = left + right
    return tree[i]

# 전체 다 바꾸니까 터지는 듯?
def change(start, end, i, b, c):
    # 범위
    if end < b or start > b:
        return
    
    tree[i] += c - arr[b]
    if start == end:
        return

    mid = (start + end) // 2
    change(start, mid, i * 2, b, c)
    change(mid + 1, end, i * 2 + 1, b, c)



def find(start, end, i, left, right):
    if end < left or start > right:
        return 0
    if left <= start and right >= end:
        return tree[i]
    mid = (start + end) // 2
    l, r = find(start, mid, i * 2, left, right), find(mid + 1, end, i * 2 + 1, left, right)
    return l + r

N, M, K = map(int, input().strip().split())
arr = [int(input().strip()) for _ in range(N)]
tree = [0] * (N * 4)

segment_tree(0, N - 1, 1)

for _ in range(M + K):
    a, b, c = map(int, input().strip().split())
    if a == 1:
        change(0, N - 1, 1, b - 1, c)
        # 원래 배열도 업데이트 해야하네 아ㅗㅁ나어로미낭ㄹ미ㅏㄴ어리ㅏㅓㅁ
        arr[b - 1] = c
    elif a == 2:
        print(find(0, N - 1, 1, b - 1, c - 1))
    # print(tree)