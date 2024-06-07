from collections import deque

def bfs(buckets):
    q = deque()
    visited.add(buckets)
    q.append(buckets)
    
    while q:
        a, b, c = q.popleft()
        # a가 0이면 C 추가
        if a == 0:
            answer.add(c)
            
        # 한 통이 빌 때까지 물 옮기기
        if a != 0:
            if a + b <= B:
                if (0, a + b, c) not in visited:
                    q.append((0, a + b, c))
                    visited.add((0, a + b, c))
            if a + c <= C:
                if (0, b, a + c) not in visited:
                    q.append((0, b, a + c))
                    visited.add((0, b, a + c))
        if b != 0:
            if a + b <= A:
                if (a + b, 0, c) not in visited:
                    q.append((a + b, 0, c))
                    visited.add((a + b, 0, c))
            if b + c <= C:
                if (a, 0, b + c) not in visited:
                    q.append((a, 0, b + c))
                    visited.add((a, 0, b + c))
        if c != 0:
            if a + c <= A:
                if (a + c, b, 0) not in visited:
                    q.append((a + c, b, 0))
                    visited.add((a + c, b, 0))
            if b + c <= B:
                if (a, b + c, 0) not in visited:
                    q.append((a, b + c, 0))
                    visited.add((a, b + c, 0))
        # 한 통이 꽉 찰 때까지 옮기기
        if a != 0:
            if a + b >= B:
                if (a + b - B, B, c) not in visited:
                    q.append((a + b - B, B, c))
                    visited.add((a + b - B, B, c))
            if a + c >= C:
                if (a + c - C, b, C) not in visited:
                    q.append((a + c - C, b, C))
                    visited.add((a + c - C, b, C))
        if b != 0:
            if a + b >= A:
                if (A, b + a - A, c) not in visited:
                    q.append((A, b + a - A, c))
                    visited.add((A, b + a - A, c))
            if b + c >= C:
                if (a, b + c - C, C) not in visited:
                    q.append((a, b + c - C, C))
                    visited.add((a, b + c - C, C))
        if c != 0:
            if a + c >= A:
                if (A, b, c + a - A) not in visited:
                    q.append((A, b, c + a - A))
                    visited.add((A, b, c + a - A))
            if b + c >= B:
                if (a, B, c + b - B) not in visited:
                    q.append((a, B, c + b - B))
                    visited.add((a, B, c + b - B))
            
        # print(a, b, c)
A, B, C = map(int, input().split())

# bfs를 통해?
visited = set()
answer = set()
bfs((0, 0, C))
answer = sorted(list(answer))
print(*answer)