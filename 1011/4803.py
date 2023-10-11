import sys
sys.stdin = open('input.txt')
# 2차원 배열로 만들어서 해보자

def dfs(i):
    global tree
    for j in range(0, len(arr[i])):
        print(i, j, arr[i][j])
        # 방문한 곳이면 두 정점에 대해 경로가 유일하지 않다는 것이므로
        if visited2[i] == 1:
            tree = False
            return
        # 방문 표시 후 재귀
        visited2[i] = 1
        visited1[i] = 1
        dfs(arr[i][j])
        visited2[i] = 0
    
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
        # 오름차순으로 정렬
        a, b = min(a, b), max(a, b)
        arr[a].append(b)
        arr[b].append(a)
    # print(arr)
    # 모든 정점이 연결되어 있으면서 임의의 두 정점에 대해 경로가 유일한 것이 트리이므로
    # dfs를 통해 연결했을 때 다시 방문한 곳에 재방문하게 된다면 트리가 아닐 것
    cnt = 0
    visited1 = [0] * (n + 1)
    visited2 = [0] * (n + 1)
    for i in range(1, n + 1):
        # 아직 방문하지 않은 곳이면
        if visited1[i] == 0:
            tree = True
            dfs(i)
            # 만약 트리이면
            if tree == True:
                # 트리 개수 추가
                cnt += 1
            print(cnt)
                
    if cnt == 0:
        print(f'Case {case}: No trees.')
    elif cnt == 1:
        print(f'Case {case}: There is one tree.')
    else:
        print(f'Case {case}: A forest of {cnt} trees.')