import sys
sys.stdin = open('input.txt')

def bfs(i):
    global tree
    q = []
    q.append(i)

    while q:
        p = q.pop(0)
        # 앞에서 방문한 곳을 다시 방문한다면 경로가 유일하지 않아 트리가 아니므로
        if visited[p] == 1:
            tree = False
        
        # 방문 표시
        visited[p] = 1
        # 간선으로 연결된 부분 중에서
        for j in arr[p]:
            # 이미 연결된 부분을 제외하고
            if visited[j] == 0:
                # 큐에 추가
                q.append(j)

case = 0
while True:
    case += 1
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    
    # 간선 리스트 - 정점은 1번부터 시작하므로
    arr = [[] for _ in range(n + 1)]
    for _ in range(m):
        (a, b) = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)
    # print(arr)
    # 모든 정점이 연결되어 있으면서 임의의 두 정점에 대해 경로가 유일한 것이 트리이므로
    # bfs를 통해 연결했을 때 다시 방문한 곳에 재방문하게 된다면 트리가 아닐 것
    cnt = 0
    visited = [0] * (n + 1)
    for i in range(1, n + 1):
        # 아직 방문하지 않은 곳이면
        if visited[i] == 0:
            tree = True
            bfs(i)
            # 만약 트리이면
            if tree == True:
                # 트리 개수 추가
                cnt += 1
            # print(cnt)
                
    if cnt == 0:
        print(f'Case {case}: No trees.')
    elif cnt == 1:
        print(f'Case {case}: There is one tree.')
    else:
        print(f'Case {case}: A forest of {cnt} trees.')