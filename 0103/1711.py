import sys
from itertools import combinations
import math
input = sys.stdin.readline

N = int(input().strip())
# 벡터 내적으로 해야겠다
arr = set()
for _ in range(N):
    v = tuple(map(int, input().strip().split()))
    arr.add(v)
        
arr = list(arr)

def inner_product(a, b, c):
    if a[0] * b[0] + a[1] * b[1] == 0:
        return 1
    elif a[0] * c[0] + a[1] * c[1] == 0:
        return 1
    elif b[0] * c[0] + b[1] * c[1] == 0:
        return 1
    else:
        return 0
    
cnt = 0
def counting(arr):
    global cnt
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                a, b, c = (arr[i][0] - arr[j][0], arr[i][1] - arr[j][1]), (arr[i][0] - arr[k][0], arr[i][1] - arr[k][1]), (arr[k][0] - arr[j][0], arr[k][1] - arr[j][1])
                cnt += inner_product(a, b, c)

counting(arr)         
print(cnt)