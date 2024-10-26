import sys
input = sys.stdin.readline
from collections import deque

def makeRing(k):
    global cnt
    q = deque()
    q.append(k)
    
    while q:
        p = q.popleft()
        visited.add(p)
        if link[p] == k:
            cnt += 1
            return
        q.append(link[p])
        
i = 1
while True:
    N = int(input().strip())
    if N == 0:
        exit()
    
    link = {}
    for _ in range(N):
        a, b = map(str, input().strip().split())
        link[a] = b
            
    cnt = 0
    visited = set()
    for k in link.keys():
        if k not in visited:
            makeRing(k)
    print(i, cnt)
    i += 1