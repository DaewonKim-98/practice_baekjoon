from collections import deque

def fromStoT(s):
    q = deque()
    q.append((s * s, '*'))
    q.append((s + s, '+'))
    # t가 2의 제곱수라면 / 연산 이후 계속 다른 연산을 한 것이므로
    q.append((1, '/'))
    visited = set()
    visited.add(s * s)
    visited.add(s + s)
    visited.add(1)

    while q:
        num, cal = q.popleft()
        # t가 되면
        if num == t:
            print(cal)
            return
        
        # * + 제외한 나머지 연산은 할 필요 없음
        if num * num <= 1000000000 and num * num not in visited:
            q.append((num * num, cal + '*'))
            visited.add(num * num)
        if num + num <= 1000000000 and num + num not in visited:
            q.append((num + num, cal + '+'))
            visited.add(num + num)

    print(-1)

s, t = map(int, input().split())
if s == t:
    print(0)
else:
    fromStoT(s)
