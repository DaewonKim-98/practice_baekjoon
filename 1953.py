from collections import deque

def otherTeam(i):
    q = deque()
    q.append((i, 0))
    
    while q:
        i, cnt = q.popleft()
        if cnt % 2 == 0:
            team1.append(i)
        else:
            team2.append(i)
        
        for j in notLike[i]:
            if visited[j] == 0:
                visited[j] = 1
                q.append((j, cnt + 1))

N = int(input())
notLike = [set() for _ in range(N + 1)]
for i in range(1, N + 1):
    arr = list(map(int, input().split()))
    for j in arr[1:]:
        notLike[i].add(j)
        notLike[j].add(i)

visited = [0] * (N + 1)
# 좋아하지 않는 사람들 다른 팀
team1 = []
team2 = []
for i in range(1, N + 1):
    if visited[i] == 0:
        visited[i] = 1
        otherTeam(i)
team1.sort()
team2.sort()
print(len(team1))
for i in team1:
    print(i, end=' ')
print()
print(len(team2))
for i in team2:
    print(i, end=' ')
print()