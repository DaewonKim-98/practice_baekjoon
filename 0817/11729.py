import sys
input = sys.stdin.readline

N = int(input().strip())

# 하노이 횟수
def hanoi_cnt(N):
    if N == 1:
        return 1
    else:
        result = hanoi_cnt(N - 1) * 2 + 1
        return result
    
# 하노이 과정
def hanoi_pro(N):
    if N == 1:
        return [(1, 3)]
    elif N == 2:
        return [(1, 2), (1, 3), (2, 3)]
    