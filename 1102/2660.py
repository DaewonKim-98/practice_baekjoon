def bfs(i):
    global min_score
    visited = [0] * (N + 1)
    q = []
    visited[i] = 1
    q.append(i)

    while q:
        p = q.pop(0)
        for j in arr[p]:
            if visited[j] == 0:
                q.append(j)
                visited[j] = visited[p] + 1

    score = max(visited) - 1
    if min_score > score:
        min_score = score
    return score


N = int(input())
arr = [[] for _ in range(N + 1)]

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    arr[a].append(b)
    arr[b].append(a)

# 모든 회원을 다 돌면서 bfs를 통해 친구의친구의친구의...친구인지 탐색해서 점수를 매기면
# 가장 깊숙하게 있는 친구의 수가 그 회원의 점수이므로 그 점수가 가장 작은 사람들을 찾으면 될듯
min_score = 50
# 회원의 점수를 나타내는 리스트, 인덱스 0은 0으로 그냥 두고 시작
scores = [0]
for i in range(1, N + 1):
    scores.append(bfs(i))

print(min_score, scores.count(min_score))
# 회원의 점수가 최솟값이면 그 회원의 번호, 즉 인덱스 출력
for i in range(1, N + 1):
    if scores[i] == min_score:
        print(i, end=' ')

