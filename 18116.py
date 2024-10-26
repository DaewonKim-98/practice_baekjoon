import sys
from collections import deque
input = sys.stdin.readline

def find(x):
    # 부모가 자신이 아니면
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# 공통 조상을 만들어주기
def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
        robot[a] += robot[b]
    elif b < a:
        parent[a] = b
        robot[b] += robot[a]
                
N = int(input().strip())
parent = [i for i in range(1000001)]
robot = [1] * 1000001
for _ in range(N):
    arr = list(map(str, input().strip().split()))
    if arr[0] == 'I':
        union(int(arr[1]), int(arr[2]))
    else:
        # 가장 부모의 부품 갯수가 연결된 부품의 갯수
        p = find(int(arr[1]))
        print(robot[p])