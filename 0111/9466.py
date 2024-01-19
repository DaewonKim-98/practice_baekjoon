import sys
input = sys.stdin.readline
<<<<<<< HEAD
sys.setrecursionlimit(10**6)

def dfs(i, student, cnt):
    global team
    # 다시 자신을 만나면 팀이 되는 것이므로
    if i == student:
        team += cnt
        for j in members:
            visited[j] = 1
        return
    
    # 지나지 않았으면 연결된 학생으로
    if student not in members:
        members.add(student)
        dfs(i, arr[student] - 1, cnt + 1)
=======
# sys.setrecursionlimit(10**6)

def dfs(i):
    global team
    visited[i] = 1
    members.append(i)
    student = arr[i] - 1
    # 방문했으면
    if visited[student] == 1:
        # 방문했는데 얘가 이 멤버 안에 있으면 얘 이후는 다 연결 되어 있다는 것?
        if student in members:
            team += len(members[members.index(student):])
        return
    
    dfs(student)
>>>>>>> e9b01ee4ee894a5aa3f6d3ee57afb55d3829242a


T = int(input())
for case in range(1, T + 1):
    N = int(input().strip())
    arr = list(map(int, input().strip().split()))

    # 연결 되는 것을 찾으면 그게 팀
    students = list(range(1, N + 1))
    # 팀인 사람들
    team = 0
    visited = [0] * N
    
    # 돌면서 찾기
    for i in range(N):
        if visited[i] == 0:
<<<<<<< HEAD
            members = set()
            dfs(i, i, 0)
=======
            members = []
            dfs(i)
>>>>>>> e9b01ee4ee894a5aa3f6d3ee57afb55d3829242a
            
    print(N - team)