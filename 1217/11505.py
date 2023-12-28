# 이젠 쉽다 쉬워 easy 쎄그먼트 뜨리 커몬 드루와라 짜식아
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def make_tree(start, end, i):
    if start == end:
        segment_tree[i] = arr[start]
        return segment_tree[i]
    
    mid = (start + end) // 2
    segment_tree[i] = (make_tree(start, mid, i * 2) * make_tree(mid + 1, end, i * 2 + 1))  % 1000000007
    return segment_tree[i]

def update_tree(start, end, i):
    # 범위 벗어나면 버려
    if b < start or end < b:
        return
    # 암ㄴ아ㅣㄻ ㅣㅏㅗㅁㄴ아러미나ㅓ업데이트 다시 만드니까 되네 ㅁ아로미나
    if start == end:
        segment_tree[i] = c
        return
    
    mid = (start + end) // 2
    update_tree(start, mid, i * 2)
    update_tree(mid + 1, end, i * 2 + 1)
    segment_tree[i] = (segment_tree[i * 2] * segment_tree[i * 2 + 1]) % 1000000007
    return 

def find(start, end, i, b, c):
    if end < b or c < start:
        return 1
    
    elif b <= start and end <= c:
        if segment_tree[i] < 0:
            return 0
        return segment_tree[i] % 1000000007
    
    mid = (start + end) // 2
    left, right = find(start, mid, i * 2, b, c), find(mid + 1, end, i * 2 + 1, b, c)
    return (left * right) % 1000000007

N, M, K = map(int, input().strip().split())
arr = [int(input()) for _ in range(N)]
segment_tree = [0] * (N * 4)

make_tree(0, N - 1, 1)

for _ in range(M + K):
    a, b, c = map(int, input().strip().split())
    # print(segment_tree)
    if a == 1:
        b -= 1
        update_tree(0, N - 1, 1)
        if c == 0:
            arr[b] = -arr[b]
        else:
            arr[b] = c
        
    else:
        print(find(0, N - 1, 1, b - 1, c - 1))